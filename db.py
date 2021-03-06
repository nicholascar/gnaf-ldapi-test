import os
from collections import defaultdict
from psycopg2 import pool
from contextlib import contextmanager
from psycopg2.pool import PoolError
from threading import Lock

from _config import DB_HOST, DB_PORT, DB_DBNAME, DB_USR, DB_PWD

class ThrottledConnectionPool(pool.ThreadedConnectionPool):
    def __init__(self, *args, seconds=1, retries=4, **kwargs):
        super(ThrottledConnectionPool, self).__init__(*args, **kwargs)
        self.seconds = seconds
        self.retries = retries

    def getconn(self, key=None):
        sleep_time = int(self.seconds)
        for r1 in range(int(self.retries)):
            for r2 in range(int(self.retries)):
                try:
                    con = super(ThrottledConnectionPool, self).getconn(key)
                    return con
                except PoolError as pe:
                    pe_args = pe.args
                    if len(pe_args) > 0 and "exhausted" in pe_args[0]:
                        import time
                        print("Throttling pg connections {} second/s".format(str(sleep_time)))
                        time.sleep(sleep_time)
                    else:
                        raise pe
                except Exception as e:
                    raise e
            print("Throttling Harder {} of {}.".format(r1+1, self.retries))
            sleep_time = sleep_time * 2
        raise RuntimeError("Still cannot get pg connection even after throttling.")


connect_str = "host='{}' port='{}' dbname='{}' user='{}' password='{}'" \
    .format(DB_HOST, DB_PORT, DB_DBNAME, DB_USR, DB_PWD)

per_process_pools = {}
per_process_mutexes = {}

def get_process_connection_pool():
    pid = os.getpid()
    if pid in per_process_pools:
        return per_process_pools[pid]
    else:
        if pid in per_process_mutexes:
            m = per_process_mutexes[pid]
        else:
            per_process_mutexes[pid] = m = Lock()
        acquired = m.acquire(blocking=True)
        assert acquired
        try:
            # Now we have the lock, we need to check again to see if another thread didn't create
            # the pool while we were waiting.
            if pid in per_process_pools:
                return per_process_pools[pid]
            print("Attempting to create a new DB connection pool for PID {}".format(pid))
            con_pool = ThrottledConnectionPool(minconn=4, maxconn=24, dsn=connect_str)
        except Exception as e:
            print("Can't connect to DB {}".format(DB_DBNAME))
            print(e)
            raise e
        finally:
            m.release()
        per_process_pools[pid] = con_pool
        print("Got it.")
        return con_pool


@contextmanager
def get_db_connection():
    con = None
    con_pool = get_process_connection_pool()
    try:
        try:
            con = con_pool.getconn()
        except Exception as e:
            print("Can't get a db connection from the connection pool.".format(DB_DBNAME))
            raise e
        yield con
    finally:
        if con is not None:
            con_pool.putconn(con)

cursor_pools = defaultdict(list)

@contextmanager
def get_db_cursor(con=None):
    put_con = False
    con_pool = None
    if con is None:
        con_pool = get_process_connection_pool()
        try:
            con = con_pool.getconn()
            put_con = True
        except Exception as e:
            print("Can't get a db cursor from the cursor pool.")
            raise e

    con_id = id(con)
    cursor_pool = cursor_pools[con_id]
    cur = None
    try:
        try:
            cur = cursor_pool.pop(0)
        except IndexError:
            try:
                cur = con.cursor()
            except Exception as e:
                print("Can't get a cursor from the connection.")
                print(e)
        yield cur
    finally:
        if cur is not None:
            cursor_pool.append(cur)
        if put_con and con_pool:
            con_pool.putconn(con)


class reg(object):
    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row):
            setattr(self, attr, val)

COPY gnaf.address_alias_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_ADDRESS_ALIAS_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.address_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_ADDRESS_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.flat_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_FLAT_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.geocode_reliability_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_GEOCODED_LEVEL_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.geocode_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_GEOCODE_RELIABILITY_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.geocoded_level_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_GEOCODE_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.level_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_LEVEL_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.locality_alias_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_LOCALITY_ALIAS_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.locality_class_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_LOCALITY_CLASS_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.mb_match_code_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_MB_MATCH_CODE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.ps_join_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_PS_JOIN_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.street_class_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_STREET_CLASS_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.street_locality_alias_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_STREET_LOCALITY_ALIAS_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.street_suffix_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_STREET_SUFFIX_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
COPY gnaf.street_type_aut FROM '{PSV_FOLDERS_DIR}Authority Code/Authority_Code_STREET_TYPE_AUT_psv.psv' WITH (format csv, header true, delimiter E'|', NULL '');
create table if not exists {{ params["table"] }} (
    "date"         datetime,
    "localName"    varchar(400),
    "name"         varchar(400),
    "countryCode"  varchar(400),
    "fixed"        boolean,
    "global"       boolean,
    "countries"    varchar(4000),
    "launchYear"   integer,
    "types"        varchar(4000)
);
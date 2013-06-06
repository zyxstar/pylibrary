CREATE TABLE LIM_BOOKINS(
    bookinsid   char(20)       PRIMARY KEY NOT NULL,
    insdt       timestamp      NOT NULL,
    insby       varchar(30)    DEFAULT 'sys' NOT NULL,
    upddt       timestamp      NOT NULL,
    updby       varchar(30)    DEFAULT 'sys' NOT NULL,
    inssts      char(10)       DEFAULT '0' NOT NULL,
    bookclsid   char(20)       NOT NULL,
    placecd     char(10)       NULL,
    readerid    char(10)       NULL
);
CREATE INDEX LIM_BOOKINS_idx1 ON LIM_BOOKINS(bookclsid);
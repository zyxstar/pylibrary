CREATE TABLE LIT_BORRNOW(
    bookinsid     char(20)       PRIMARY KEY NOT NULL,
    insdt         timestamp      NOT NULL,
    insby         varchar(30)    DEFAULT 'sys' NOT NULL,
    upddt         timestamp      NOT NULL,
    updby         varchar(30)    DEFAULT 'sys' NOT NULL,
    readerid      char(20)       NOT NULL,
    readercardno  char(20)       NOT NULL,    
    borrdt        timestamp      NULL,
    borrexpdt     timestamp      NULL,
    renewtimes    integer        DEFAULT 0 NULL
);
CREATE INDEX LIT_BORRNOW_idx1 ON LIT_BORRNOW(readerid);
CREATE INDEX LIT_BORRNOW_idx3 ON LIT_BORRNOW(readercardno);
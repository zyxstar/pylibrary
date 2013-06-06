CREATE TABLE LIT_BORRHIS(
    borrhisid     char(36)          PRIMARY KEY NOT NULL,
    insdt         timestamp         NOT NULL,
    insby         varchar(30)       DEFAULT 'sys' NOT NULL,
    upddt         timestamp         NOT NULL,
    updby         varchar(30)       DEFAULT 'sys' NOT NULL,
    readerid      char(20)          NOT NULL,
    readercardno  char(20)          NOT NULL,   
    bookinsid     char(20)          NOT NULL,
    borrdt        timestamp         NULL,
    borrexpdt     timestamp         NULL,
    renewtimes    integer           DEFAULT 0 NULL,
    retdt         timestamp         NULL,
	overdays      integer           DEFAULT 0 NULL,
    overprice     decimal(10, 2)    DEFAULT 0 NULL,
	overpaycd     char(10)          NULL,
    defaceprice   decimal(10, 2)    DEFAULT 0 NULL,
	defacepaycd   char(10)          NULL,
	defacenote    nvarchar(1000)    NULL,
    lostprice     decimal(10, 2)    DEFAULT 0 NULL,
	lostpaycd     char(10)          NULL,
	lostnote      nvarchar(1000)    NULL
);
CREATE INDEX LIT_BORRHIS_idx1 ON LIT_BORRHIS(readerid);
CREATE INDEX LIT_BORRHIS_idx2 ON LIT_BORRHIS(bookinsid);
CREATE INDEX LIT_BORRHIS_idx3 ON LIT_BORRHIS(readercardno);
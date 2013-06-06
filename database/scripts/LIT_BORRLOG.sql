CREATE TABLE LIT_BORRLOG(
    borrlogid    integer PRIMARY KEY AUTOINCREMENT,
    insdt        timestamp         NOT NULL,
    insby        varchar(30)       DEFAULT 'sys' NOT NULL,
	borrhisid    char(36)          NULL,
    readercardno char(20)          NULL,	
    readerid     char(20)          NULL,
    readername   nvarchar(30)      NULL,
    bookinsid    char(20)          NULL,
    bookclsid    char(20)          NULL,
    bookname     nvarchar(200)     NULL,
    actcd        char(10)          NULL,
	actval       decimal(10, 2)    NULL,
	paycd        char(10)          NULL,
    note         nvarchar(1000)    NULL
);
CREATE INDEX LIT_BORRLOG_idx1 ON LIT_BORRLOG(insdt);
CREATE INDEX LIT_BORRLOG_idx2 ON LIT_BORRLOG(insby);
CREATE INDEX LIT_BORRLOG_idx3 ON LIT_BORRLOG(readercardno);
CREATE INDEX LIT_BORRLOG_idx4 ON LIT_BORRLOG(readerid);
CREATE INDEX LIT_BORRLOG_idx5 ON LIT_BORRLOG(actcd);
CREATE INDEX LIT_BORRLOG_idx6 ON LIT_BORRLOG(borrhisid);
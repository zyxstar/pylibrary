CREATE TABLE LIM_BOOKCLS(
    bookclsid       char(20)          PRIMARY KEY NOT NULL,
    insdt           timestamp         NOT NULL,
    insby           varchar(30)       DEFAULT 'sys' NOT NULL,
    upddt           timestamp         NOT NULL,
    updby           varchar(30)       DEFAULT 'sys' NOT NULL,
    clssts          char(10)          DEFAULT '0' NOT NULL,    
    isbn            char(20)          NULL,
    bookname        nvarchar(200)     NULL,
    price           decimal(10, 2)    DEFAULT 0 NULL,
    pubcd           char(10)          NULL,
    auth            nvarchar(200)     NULL,
    catcd           char(10)          NULL
);
CREATE INDEX LIM_BOOKCLS_idx1 ON LIM_BOOKCLS(isbn);
CREATE INDEX LIM_BOOKCLS_idx2 ON LIM_BOOKCLS(bookname);
CREATE INDEX LIM_BOOKCLS_idx3 ON LIM_BOOKCLS(catcd);
CREATE INDEX LIM_BOOKCLS_idx4 ON LIM_BOOKCLS(clssts);
CREATE INDEX LIM_BOOKCLS_idx5 ON LIM_BOOKCLS(auth);
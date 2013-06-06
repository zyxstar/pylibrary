CREATE TABLE LIC_READERTYP(
    readertypcd   char(10)          PRIMARY KEY NOT NULL,
    insdt         timestamp         NOT NULL,
    insby         varchar(30)       DEFAULT 'sys' NOT NULL,
    upddt         timestamp         NOT NULL,
    updby         varchar(30)       DEFAULT 'sys' NOT NULL,
    typname       nvarchar(30)      NULL,
    typquantity   integer           DEFAULT 0 NULL,
    typdtlimit    integer           DEFAULT 0 NULL,
    typoverprice  decimal(10, 2)    DEFAULT 0 NULL,
    typdeposit    decimal(10, 2)    DEFAULT 0 NULL,
    typborrcat    varchar(2000)     NULL,
    typrenewtimes integer           DEFAULT 0 NULL,
    typrenewterm  integer           DEFAULT 0 NULL,
    typlostpay    decimal(10, 2)    DEFAULT 0 NULL
);
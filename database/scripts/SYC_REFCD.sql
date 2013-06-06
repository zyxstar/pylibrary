CREATE TABLE SYC_REFCD( 
    grp      varchar(30)       NOT NULL,
    cd       varchar(30)       NOT NULL,
    insdt    timestamp         NOT NULL,
    insby    varchar(30)       DEFAULT 'sys' NOT NULL,
    upddt    timestamp         NOT NULL,
    updby    varchar(30)       DEFAULT 'sys' NOT NULL,
    recsts   char(10)          DEFAULT '0' NOT NULL, 
    sdesc    nvarchar(200)     NOT NULL,
    fdesc    nvarchar(1000)    NULL,
    var1     nvarchar(200)     NULL,
    var2     nvarchar(200)     NULL,
    var3     nvarchar(200)     NULL,
    ordseq   decimal(10, 2)    NULL,
    CONSTRAINT PK_bookcls PRIMARY KEY (grp,cd)
);

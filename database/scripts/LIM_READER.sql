CREATE TABLE LIM_READER(
    readerid     char(20)          PRIMARY KEY NOT NULL,
    insdt        timestamp         NOT NULL,
    insby        varchar(30)       DEFAULT 'sys' NOT NULL,
    upddt        timestamp         NOT NULL,
    updby        varchar(30)       DEFAULT 'sys' NOT NULL,
    readertypcd  char(10)          NOT NULL, 
    readercardno char(20)          NOT NULL, 
    readername   nvarchar(30)      NULL,
    gender       char(1)           NULL,
    bob          timestamp         NULL,
    iccd         char(10)          NULL,
    icno         varchar(30)       NULL,
    orgcd        char(10)          NULL,
    tel          varchar(30)       NULL,
    email        varchar(50)       NULL,
    deposit      decimal(10, 2)    DEFAULT 0 NULL,
    quantity     integer           DEFAULT 0 NULL,
    note         nvarchar(1000)    NULL
);
CREATE INDEX LIM_READER_idx1 ON LIM_READER(readername);
CREATE INDEX LIM_READER_idx2 ON LIM_READER(orgcd);
CREATE INDEX LIM_READER_idx3 ON LIM_READER(readertypcd);
CREATE INDEX LIM_READER_idx4 ON LIM_READER(readercardno);
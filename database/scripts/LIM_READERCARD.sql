CREATE TABLE LIM_READERCARD(
    readercardno    char(20)          PRIMARY KEY NOT NULL,
    insdt           timestamp         NOT NULL,
    insby           varchar(30)       DEFAULT 'sys' NOT NULL,
    upddt           timestamp         NOT NULL,
    updby           varchar(30)       DEFAULT 'sys' NOT NULL,
    cardsts         char(10)          DEFAULT '0' NOT NULL,
    readerid        char(20)          NOT NULL,    
    issdt           timestamp         NULL,
    expdt           timestamp         NULL,
    canceldt        timestamp         NULL,
    operator        varchar(30)       NULL,
    note            nvarchar(1000)    NULL
);
CREATE INDEX LIM_READERCARD_idx1 ON LIM_READERCARD(readerid);

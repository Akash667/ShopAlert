create table if not exists users(
    UID int PRIMARY KEY,

);

create table if not exists products(
    PID int PRIMARY KEY,
    pname varchar(255) not null,
    URL varchar(255) unique,
    date_added datetime,
);

create table if not exists userproductrelation(
    UID int NOT NULL,
    PID int NOT NULL,
    FOREIGN KEY (UID) REFERENCES users(UID),
    FOREIGN KEY (PID) REFERENCES products(PID)
);

create table if not exists prices(
    PID int,
    currentdate datetime DEFAULT(CURRENT_DATE()),
    price Decimal(10, 2),
    FOREIGN KEY (PID) REFERENCES products(PID),
    PRIMARY KEY (PID, currentdate)
);

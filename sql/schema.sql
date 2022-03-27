
drop table if exists cal;
create table if not exists cal (
    id int primary key,
    x int not null,
    y int not null
);

-- TODO: insert initial data
insert into cal values(1, 50, 500);
insert into cal values(2, 100, 1000);
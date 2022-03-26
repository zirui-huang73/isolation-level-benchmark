
drop table if exists cal;
create table if not exists cal (
    id int primary key,
    x int not null,
    y int not null
);

-- TODO: insert initial data
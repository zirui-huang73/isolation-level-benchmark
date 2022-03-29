
drop table if exists cal;
create table if not exists cal (
    id bigint primary key,
    x int not null,
    y int not null,
    z text
);

-- TODO: insert initial data
insert into cal values(1, 50, 500, 'male');
insert into cal values(2, 100, 1000, 'female');
insert into cal values(3, 60, 600, 'male');
insert into cal values(4, 110, 1200, 'female');
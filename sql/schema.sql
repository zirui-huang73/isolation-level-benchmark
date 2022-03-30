
drop table if exists cal;
create table if not exists cal (
    id bigint primary key,
    x int not null,
    y int not null,
    z text
);

insert into cal values(1, 30, 10, 'male');
insert into cal values(2, 100, 1000, 'female');
insert into cal values(3, 60, 600, 'male');
insert into cal values(4, 110, 1200, 'female');

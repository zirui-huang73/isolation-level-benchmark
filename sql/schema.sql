CREATE OR REPLACE FUNCTION random_between(low INT, high INT) 
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random() * (high-low + 1) + low);
END;
$$ language 'plpgsql' STRICT;

drop table if exists cal;
create table if not exists cal (
    id bigint primary key,
    x int not null,
    y int not null,
    z text
);

do $$
begin
for loop_cnt in 1..10000 loop
    if loop_cnt % 2 = 0
    then
        insert into cal values(loop_cnt, loop_cnt, random_between(1, 10000), 'male');
    else
        insert into cal values(loop_cnt, loop_cnt, random_between(1, 10000), 'female');
    end if;
end loop;
end; $$
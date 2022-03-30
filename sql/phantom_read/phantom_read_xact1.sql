
begin transaction;

set transaction isolation level read committed;
select * from employees where gender = 'Male';

select pg_sleep(5);

select * from employees where gender = 'Male';

commit transaction;


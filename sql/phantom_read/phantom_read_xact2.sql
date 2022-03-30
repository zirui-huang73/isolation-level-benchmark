
begin transaction;

set transaction isolation level read committed;

insert into employees values (1005, 'Sambit', 'Male');

commit transaction;


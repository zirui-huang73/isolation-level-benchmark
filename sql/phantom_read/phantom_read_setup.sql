drop table if exists employees;

create table if not exists employees (
	id int primary key,
	name varchar (100),
	gender varchar (10)
);

insert into employees values (1001, 'Anurag', 'Male');
insert into employees values (1002, 'Priyanka', 'Female');
insert into employees values (1003, 'Pranaya', 'Male');
insert into employees values (1004, 'Hina', 'Female');

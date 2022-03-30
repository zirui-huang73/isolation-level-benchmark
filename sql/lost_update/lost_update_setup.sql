
drop table if exists products;

create table if not exists products (
	id int primary key,
	name varchar(50) not null,
	itemsInStock int not null
);

insert into products values
	(1, 'Laptop', 12),
	(2, 'Iphon', 15),
	(3, 'Tablets', 10);


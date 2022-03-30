
begin transaction;

set transaction isolation level serializable;

select itemsInStock from products where id = 1;

select pg_sleep(10);

update products set itemsInStock = itemsInStock - 2 where id = 1;

select itemsInStock from products where id = 1;

commit;

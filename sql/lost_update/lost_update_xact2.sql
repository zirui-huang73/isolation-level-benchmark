
begin transaction;

set transaction isolation level serializable;

select itemsInStock from products where id = 1;

update products set itemsInStock = itemsInStock - 3 where id = 1;

select itemsInStock from products where id = 1;

commit;

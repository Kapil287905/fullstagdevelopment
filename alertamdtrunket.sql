show databases;
use amazon;
show tables;
select * from customers;

-- drop (deleting db and table)
drop database az1;
drop schema db2;

create table customers1 as select * from customers; -- subquery
select * from customers1;

create table customers2 as select * from customers;
select * from customers1;

drop table customers2; -- delete table
-- drop table customers2; error unknown table

-- truncate (use to remove values/row/tuples from tables)
select * from customers1;
truncate table customers1;
select * from customers1;

-- alter (modify,change,drop,add,rename)
alter table customers add country varchar(20);
desc customers;
select * from customers;

-- alter table customers add newcolum datatype fitst|after;
-- WAQ to add aadharnumber column at first in custormers table
alter table customers add aadharnum bigint first;
desc customers; 

-- WAQ to add city column at before in address table
alter table customers add city varchar(20) after mobile;
desc customers;

-- WAQ to add liscencenum and age column in address table
alter table customers add (licencemun int,age int);
desc customers;

-- drop colum
alter table customers drop aadharnum;
desc customers;

-- alter table customers drop(address,licensenum,age); -- syntax error
alter table customers drop city;
alter table customers drop licencemun;
alter table customers drop age;
desc customers;

-- modify (changing datatype)
-- WAQ to change datatype of lname to car(50) in custormers table
alter table customers modify lname char(50);
desc customers;

-- WAQ to change datatype of cid to varchar(50) in custormers table
alter table customers modify cid varchar(50);
desc customers;

-- alter table customers modify fname int; -- error char to int not possible
select * from customers;

insert into customers(cid) values('A123');
select * from customers;
alter table customers modify cid int;
select * from customers;

-- change(column name change/renameing name)
-- WAQ to change column name dob to dateofbirth in custormers table
alter table customers change dob dateofbirth date;

-- WAQ to change column name fname to firstname char(50) in custormers table
alter table customers change fname firstname char(50);
select * from customers;

-- rename(renaming table name)
-- WAQ to rename table of customers to newcustomers

alter table customers rename newcustomers;
desc newcustomers;

-- rename(renaming table name)
-- WAQ to rename table of newcustomers to customers

rename table newcustomers to customers;
desc customers;




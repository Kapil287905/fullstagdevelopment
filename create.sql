create schema amazon;
show databases;
create database az1;
-- Tables (customers,products,orders,cart,payments)
-- customer (cid,fmane,lname,gender,dob,email,mobile,address)
use amazon;
create table customers
(
cid int,
fname char(20),
lname char,
gender char(10),
dob date,
email varchar(30),
mobile int,
address varchar(50)
);
desc customers;
show tables;
-- product (pid,pname,category,modelnum,price,qty,manfdate)
create table product
(
pid int,
pname varchar(30),
categoty varchar(30),
modelnum int,
qty int,
manfdate date
);
desc product;

-- orders (oid int,cid int,pid int,orderdatetime datetime,qty int,totalprice decimal(8,2))
create table orders
(
oid int,
cid int,
pid int,
orderdatetime datetime,
qty int,
totalprice decimal(8,2)
);
desc orders;

-- insert syntax
-- insert into tr_name(colname1,colname2,....) value(val1,val2,.....);
-- insert into tr_name value(val1,val2,.....);
-- insert into tr_name value(val1,val2,.....),(val1,val2,.....);

insert into customers(cid,fname,lname,gender,dob,email,mobile,address)
values(1,'komal','g','femail','2000-09-02','k@gmail.com',1297797899,'malad');

select * from customers;

insert into customers(cid,fname,gender,email)
values(2,'rohit','maler','dsdsds');

select * from customers;

desc customers;

-- insert into customers values('meena','k','fsdfsdf','2003-08-06','m@gmail.com',2,11111111,'vasai'); --error

-- insert into customers values(2,'meena','k','fsdfsdf','2003-08-06','m@gmail.com',11111111); -- error  column count

insert into customers values(2,'meena','k','fsdfsdf','2003-08-06','m@gmail.com',11111111,null);

insert into customers 
values(3,'raj',null,'male',null,null,6565767,'virar'),
(4,'raj',null,'male',null,null,6565767,null),
(5,'pooja',null,'female',null,null,6565767,'dadar');

select * from customers;

insert into customers values();

select * from customers;



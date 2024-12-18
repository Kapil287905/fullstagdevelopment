use amazon;
show tables;
select * from customers;
-- DML (update)
-- wsq to upday for all custeromers set as 'india' 
update customers set country='India';
select * from customers;

-- Wa to update country for customerid i set country 'uk'
update customers set country='UK' where cid=1;
select * from customers;

-- Wa to update lname,fname,dob mobilenadd for customerid set country 'uk'
update customers set firstname='rohit',dateofbirth='2002-04-12',email='r@gmail.com',
mobile='54334566',address='malad' where cid=2;

update customers set gender='male' where cid=2 and firstname='rohit';
select * from customers;

-- wq change datatype of mobile colum from custermers modify as bighint
alter table customers modify mobile bigint;
desc customers;

-- wq to update mobile number id 1 and 2 9874323456
update customers set mobile=9874323456 where cid in (1,2);
select * from customers;

-- wq to update country of custormer who are from malad and virar set country as 'usa'
update customers set country='USA' where address in ('malad','virar');
select * from customers;

-- wq to set address as 'Borivali' for those who address is not there in customer table
update customers set address='Borivali' where address is null;
select * from customers;

-- wq to update customers emailid those from india and usa set email as 'e@gmail.com'
update customers set email='e@gmail.com' where country='india' or country='usa';
-- or
update customers set email='e@gmail.com' where country in('india','usa');
select * from customers;

create table employeesa
(
eid int primary key,
fname char(20),
gender enum('female', 'male','other'),
dob date,
salary float,
managerid int,
deptname set('hr','admin','training','account','it'),
city varchar(2)
);

desc employeesa;

insert into employeesa values('101','rakesh','male','1999-08-12',800000,null,'ht,it','mumbai');
select * from employeesa;

insert into employeesa values('102','pooja','male','2002-1-2',600000,101,'hr,it','pune');
select * from employeesa;

insert into employeesa values('103','meena','female','2001-11-22',400000,null,'admin','indore');
select * from employeesa;
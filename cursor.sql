-- functions block of code to avoid repeation of code and called nth number time
-- 1) Aggregate function
-- 2) scalar function
-- 3) Table valued function

-- write a function calculatediscount() to show diuscounted amount by taking input as totalamount and discountamount

use amazon;
delimiter //
create function calculatediscount(totalamount float,discountper float)
returns float
deterministic
begin
declare discountamount float;
set discountamount=totalamount*(discountper/100);
return discountamount;
end //

select calculatediscount(100,10);
select calculatediscount(50,10);
select calculatediscount(89000000,45);

-- apply above funtion on emp table to show discount on salary
select eid,ename,salary,calculatediscount(salary,10) as '10% of salary' from emp;

-- write function getempbysalary() to show emp as per given lower and higher salary range
delimiter //
create function getempbysalary(lower float,higher float)
returns varchar(10000)
deterministic
begin
declare employeelist varchar(10000) default "";
select group_concat(ename separator ',') into employeelist from emp where salary between lower and higher;
return employeelist;
end //
drop function getempbysalary;
select getempbysalary(10000,50000);
select * from emp where salary between 10000 and 50000;

-- write an function salarygrade() to show upper grade and lower grade remark from 
-- salary compring with 10000 for each emp
delimiter //
create function salarygrade(sal float)
returns varchar(30)
begin
declare remark varchar(30);
if sal>10000 then
set remark="upper grade";
else
set remark="lower grade";
end if;
return remark;
end // 
select eid,ename,salary,salarygrade(salary) as "salary grade" from emp;

-- Trigger
-- it is event /action which can happen on table before of after operation like insert,update and delete
-- Systax
-- delimiter //
-- create trigger triggetname
-- before | agter
-- insert | update delete on table_name
-- for each row
-- begin
-- start1
-- start2
-- start3
-- end //

create database triggerdemo;
use triggerdemo;
create table table1(id int,name char(20));
create table table2(id int,name char(20));

-- write trigger for insert same value into table2 when insert happen on table1
select * from table1;
select * from table2;

delimiter //
create trigger trInsertTable1
after insert on table1
for each row
begin
insert into table2(id,name) value(new.id,new.name); 
end //
insert into table1 value(101,'komal');
select * from table1;
select * from table2;
insert into table1 value(102,'raj');
insert into table1 value(103,'pooja');
insert into table1 value(104,'keerti');
insert into table1 value(105,'suraj');
select * from table1;
select * from table2;

-- write trigger for table1 whenever any of the record delete deleted than it gets added in table3 which
-- has id,name,tableaction,logdatetime,username
create table table3(
id int,name char(20),
tableaction varchar(20),
logdatetime datetime,
username varchar(20)
);
select * from table3; 
select now();
select user();

delimiter //
create trigger trDeleteTable1
before delete on table1
for each row
begin
insert into table3 values(old.id,old.name,'delete',now(),user());
end //
delete from table1 where id=101;
select * from table1;
select * from table3;

-- update on table1
create table table4
(
userbane varchar(20),
description varchar(100),
logdatetime datetime
)

delimiter //
create trigger trUpdateTable1
after update on table1
for each row
begin
insert into table4 values(user(),concat('update table1 record for',old.id,'Previous Name',old.name,'New name',new.name),now()); 
end //
update table1 set name='xxxx' where id=102;
select * from table1;
select * from table4;


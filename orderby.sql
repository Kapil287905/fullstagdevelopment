use amazon;
-- distinct() clause avoid repeated calues
show tables;
select * from customers;
-- WQ to show cities of custumers where they belong
select distinct(address) from customers;
select distinct(address),country from customers;
update customers set country='UK' where cid=5;
select * from customers;

-- order by (ascending-asc and descending-desc)
select * from customers order by firstname; -- default ascending
select * from customers order by firstname asc;
select * from customers order by firstname desc;
select * from customers order by cid;
-- wq to show record as per birthday oldest to youngest.alter
select * from customers order by dateofbirth asc;

-- WQ to femail with alphabetical order
select * from customers where gender='femail' order by firstname;

-- limit clause (use to show specified row)
-- WQ to show first two record of customers
select  * from customers order by cid limit 2;

-- WQ to show last two record of customers
select  * from customers order by cid desc limit 2;

-- WQ to show only last record of customers
select  * from customers order by cid desc limit 1;

-- limit clause has offset which is used to omit the row
-- WQ to show 2nd record of customers
select  * from customers limit 1,1; -- first 1 is used to skip the row  and 2nd one is to show 1 row

-- WQ to show 6th record of customers
select  * from customers limit 5,1;

-- WQ to show 2nd last record of customers
select  * from customers order by cid desc limit 1,1;

-- WQ to show 3rd and 4th record of customers
select  * from customers;
select  * from customers limit 2,2;

-- WQ to show 2nd and 5th record of customers
(select  * from customers limit 1,1)
union
select  * from customers limit 4,1; -- showing only 5th row

select* from emp;
-- WQ show 2nd highhest salaries employee detail
select * from emp order by salary desc limit 1,1;

-- WQ show 4th to 8th row of employee but show alphabetical order
select * from emp order by eid,ename desc limit 3,5;
select * from emp limit 3,5;

-- views (virtual table used to store query result)
create view emorecord as select * from emp limit 3,5;
select* from emorecord;
select * from emorecord order by ename;

-- select case stmt it is an block where we show result as per condition matches
-- syntax
-- select col1,col2,col3, or *,
-- case
-- when codition1 than 'stmt'
-- when codition2 than 'stmt'
-- when codition3 than 'stmt'
-- else 'stmt'
-- end 'stmt'

-- from tablename

-- WQ to show remark base on salary range as salary<20000 'grade-III',
-- salary<50000 and salary>=20000 'grade-II' and salary<=80000 and salary>=50000 'grade-I'
-- for each emplouee and show  only eid,ename,salary and remark

select eid,ename,salary,
case
when salary<20000 then 'Grade III'
when salary<50000 and salary>=20000 then 'Grade II'
when salary<=80000 and salary>=50000 then 'Grade I'
else 'N/A'
end as 'Slalry Remark'
from emp;

-- show above query in view so it will easier to call multiple time
create view salarygrade
as
select eid,ename,salary,
case
when salary<20000 then 'Grade III'
when salary<50000 and salary>=20000 then 'Grade II'
when salary<=80000 and salary>=50000 then 'Grade I'
else 'N/A'
end as 'Slalry Remark'
from emp;

select* from salarygrade;

-- function (built-in) it block use to avoide repeatation of code and call n number of time
-- 3 type (math,string,)

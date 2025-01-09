-- function (built-in) it block use to avoide repeatation of code and call n number of time
-- 3 type (math,string,)
-- built in function (system define)
-- math function 1)Scalar 2)Aggregate(group function

-- Scalar function
select sqrt(50);
select power(10,6);
select pow(10,6);
select round(1111.45445443);
select round(1111.45445443); -- showing only digits and it is doing rounding of decimal point digit
select floor(1111.45445443); -- showing digit but truncating decimal point digit
use amazon;
select * from emp;

-- WQ to show employee id,name and salary with round figure
select eid,ename,round(salary) from emp;

-- WQ to show employee id,name also whose round of salary is 500000
select eid,ename,round(salary) from emp where round(salary)=500000;


select sign(455); -- when +ve then it show 1 
select sign(-455.435345); -- when -ve then it show -1 
select abs(3435);
select abs(-3435); -- it remove -ve sign
select ceil(45.1); -- next highest integral number
select ceil(45.00000001);
select mod(4,2); -- 4%2
select 4%2;
select mod(2,4); -- 2
select mod(22,4); -- 2

-- Aggregate  function / group function - generate single row answer
-- min(),max(),count(),sum(),avg()

select * from emp;
-- find total count employee
select count(*) from emp;
select count(eid) from emp;
select count(ename) from emp;
select count(email) from emp; -- count() ignores null values
desc emp;

-- find employee count whose salary is above 50000.
select count(eid) from emp where salary>50000;

-- display how many cities are there where employee are belong.
select count(city) from emp; -- wrong with repeated cities
select count(distinct(city)) from emp; -- with repeated cities

-- display lowest salary of emp
select min(salary) from emp;
select min(salary),ename from emp;
select min(salary),ename from emp where salary=(select min(salary) from emp);

-- display highest salary of emp
select max(salary) from emp;

-- display average salary of emp
select avg(salary) from emp;

-- display total of salary of all emp
select sum(salary) from emp;

-- display count of employee as per cities
select city,count(eid) from emp group by city;

-- group by clause use to show result in group byusing below thing
-- 1) group by applied only single colum which has reapeated values
-- 2) grouo by worked with aggregste/group function= min(),max(),count(),sum(),avg()
-- 3) the colum written in group by must be present in select
-- 4) group by also has having clause which not compsory
-- 5) having clause use to write condition after group by

-- Q.1)Dispaly count from employee as per gender
select gender,count(eid) from emp group by gender;

-- Q.2) Dispaly count from employee as per gender with total salary
select gender,count(eid),sum(salary) from emp group by gender;
select gender,count(eid),sum(round(salary)) from emp group by gender;
select * from emp;
-- Q.3) display emp count as per countries
select country,count(eid) from emp group by country;

-- Q.4) find emp count those who are using gmail account
select email,count(eid) from emp where email like '%gmail.com' group by email;
-- or
select email,count(eid) from emp group by email having email like '%gmail.com';

-- Q.5) show avgrange salary of employee whose birthday from 1st jan 2000 to 31st dec 2005
select avg(salary) from emp where dob between '2000-01-01' and '2005-12-31';
-- as per dob avg salary
select dob,avg(salary) from emp where dob between '2000-01-01' and '2005-12-31' group by dob;

-- Q.6) show emp sum of salaries as per cities and show emp count well
-- but show only those employee whose total of salary is above 120000

select city,count(eid),sum(salary) from emp where sum(salary)>120000 group by city; -- error because where clause giving single row and can't group by

select city,count(eid),sum(salary) from emp group by city having sum(salary)>120000;
select city,count(eid),sum(salary) from emp group by city;

-- Q.7) show emp sum of salary asy per city from mumbai and pune and show emp count as well
-- byt shoe only those totle is above 120000

select city,count(eid),sum(salary) from emp where city in('Mumbai','Pune') group by city having sum(salary)>120000;
-- or
select city,count(eid),sum(salary) from emp group by city having city in('mumbai','pune') and sum(salary)>120000;

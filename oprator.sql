use amazon;
show tables;
select database();

-- Aritimatic,relational,Logical,range,list,like,is
-- range (brtween)
select * from emp;

-- WQ ri show emp whose salary from 50k to 60k
select * from emp where salary>=50000 and salary<=60000;
-- or
select * from emp where salary between 50000 and 60000;

-- WQ ri show emp whose birthday from 1st jan 1995 to 31st jan 20000
select * from emp where dob between '1995-01-01' and '2000-01-31';
-- select * from emp where dob between '2000-01-01' and '1915-01-31'; -- it won't work because between always start from lowest

-- list operator (in,not in)
-- WQ to show emp who are from mumbai,pune and delhi
select * from emp where city='mumbai' or city='pune' or city='delhi';
-- or
select * from emp where city in ('mumbai','pune','delhi');

-- WQ to show emp whose salary is not 50000,80000 or 48000
-- select * from emp where salary!=50000 or salary!=48000 or salary!=80000; -- wrong answer rule violates

select * from emp where not (salary=55000 or salary=48000 or salary=80000); 

select * from emp where salary not in (55000,48000,80000);

-- like (pattern) %,_
-- WQ to find emp start with 'j';
select * from emp where ename like 'j%';

-- WQ to find emp end with 'n';
select * from emp where ename like '%n';

-- WQ to find emp end with 'son';
select * from emp where ename like '%son';

select * from emp;

-- WQ to find emp who are using gmailaccount;
select * from emp where email like '%gmail.com' or '%gmail.co.in';

-- WQ to find emp whose name having 2nd character as 'o';
select * from emp where ename like '_o%';

-- WQ to find emp whose name having 2nd last character as 'o';
select * from emp where ename like '%o_';

-- WQ to find emp whose name having 'ee' in between;
select * from emp where ename like '%ee%';

-- WQ to find emp whose name start  ana end with 'n';
select * from emp where ename like 'n%%n';

select * from emp;

-- WQ to find emp whose mobile start with 98.
select * from emp where mobile like '98%';

-- is null, is not null 
select * from emp;

INSERT INTO emp 
VALUES ('11','','male', 9876543299, '', 'gujrat',null, 50000,'UK');
select * from emp;

INSERT INTO emp 
VALUES ('12','kishore','male',9876543200,'kk@gmail.com', 'mumbai','1998-09-19', 50000,'USA');
select * from emp;

-- WQ  to find emp whose email is not present
-- select * from emp where email=null; -- wrong way of checking empty calue 
select * from emp where email is null or email='';

insert into emp(ename,gender,mobile,email,city,dob,salary,country)
values('shiddu','male',7878987777,null,'Pune','2000-10-21',300000,'USA');
select * from emp;

-- WQ  to find emp whose name is not present
select * from emp where ename is null or ename='';

select * from emp where ename like '';
select * from emp where email like null;
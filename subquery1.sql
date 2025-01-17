use amazon;
show tables;
-- subqoery with create,insert,update and delete

create table newemp as select * from emp where gender='female'; -- eithout key constraint
select * from newemp;
desc newemp;

-- TCL(commit,roleback,savepoint)
start transaction;
delete from newemp;
select * from newemp;
rollback;
select * from newemp;
commit;

select * from emp;
-- WQ to insert employee whose salary is grater then 10000 in newemp

insert into newemp select * from emp where salary>10000;
select * from newemp;

-- WQ to delete employee whose salary is from 10000 to 40000 in newemp but cpmpare from emp table
delete from newemp where salary in (select salary from emp where salary between 10000 and 40000);

-- WQ to update country as IN for employee who are from india from newemp but cpmpare from emp table

update newemp set country='IN' 
where country in(select country from emp where country='India');

select * from newemp;
rollback;
select * from newemp;

start transaction;
savepoint beforedelete;
-- delete emp id 1 record
delete from newemp where eid=1;
select * from newemp;

savepoint beforeupdate;
-- set salary as 2000 for id=3
update newemp set salary=20000 where eid=5; 
select * from newemp;

rollback to beforedelete;
select * from newemp;

-- views (viewa is to store result also it callrd virtual table)
create view newemp_view as select eid,ename,city,salary from newemp;
select * from newemp_view;
create view newemp1 as select * from newemp;
select * from newemp1;

-- inserting in newemp(main)
insert into newemp values(90,'aaaa','male',5345,null,'mumbai',null,null,null);
select * from newemp;
select * from newemp1;

insert into newemp1 values(91,'neel','male',555025,null,'mumbai',null,null,null);
select * from newemp1;
select * from newemp;

select * from newemp_view;
insert into newemp_view values(92,'cccc','delhi',50000);
select * from newemp_view;
select * from newemp;
desc newemp;

delete from newemp where eid=91;
select * from newemp;
select * from newemp1;

delete from newemp1 where eid=92;
select * from newemp1;
select * from newemp;

delete from newemp_view where eid=90;
select * from newemp_view;
select * from newemp;


select * from emp_age;




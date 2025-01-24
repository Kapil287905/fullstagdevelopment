use hr;
select count(employee_id)  from employees where salary>5000; 
select first_name  from employees where salary>5000 limit 5; 
-- write procedure to show employee whose salary is grater than 5000 but show only 5 records by usinf loop
delimiter //
create procedure showemp()
begin
declare i int default 1;
declare ans varchar(100) default '';
select first_name from employees where salary>5000;
while i<=5 do
set ans=concat(ans,first_name,'');
set i=i+1;
end while;
select ans;
end //

call showemp; -- wrong answer showing 58 records as apply cursor

delimiter //
create procedure showemp1(inout ans varchar(100))
begin
declare i int default 1;
declare output varchar(100) default '';
declare emplistcursor cursor for
select first_name from employees where salary>5000;
open emplistcursor;
while i<=5 do
fetch emplistcursor into output;
set ans=concat(ans,output,'');
set i=i+1;
end while;
close emplistcursor;
end //
set @ans='';
call showemp1(@ans);
select @ans;

drop procedure showemp1;

delimiter //
create procedure emp_data()
begin
declare fname varchar(50);
declare lname varchar(50);
declare emid varchar(50);
declare sal float;
declare done int default false;
declare cur1 cursor for select first_name from employees;
declare cur2 cursor for select last_name from employees;
declare cur3 cursor for select email from employees;
declare cur4 cursor for select salary from employees;
declare continue handler for not found set done=true;
open cur1;
open cur2;
open cur3;
open cur4;
go:loop
if done then
leave go;
end if;
fetch cur1 into fname;
fetch cur2 into lname;
fetch cur3 into emid;
fetch cur4 into sal;
select fname,lname,emid,sal;
end loop;
close cur1;
close cur2;
close cur3;
close cur4;
end //

call emp_data;


delimiter //
create procedure getemp_position()
begin
declare fname varchar(20);
declare lname varchar(20);
declare sal float;
declare position varchar(20);
declare done int default false;
declare cur1 cursor for
select first_name,last_name,salary from employees;
declare continue handler for not found set done=true;
open cur1;
readloop:loop
fetch cur1 into fname,lname,sal;
if done then
leave readloop;
end if;
if sal>20000 then
set position="manager";
elseif sal>=5000 and sal<20000 then
set position="associate";
elseif sal>=0 and sal<5000 then
set position="executive";
else
set position="N/A";
end if;
select fname as FirstName,lname as LastName,sal as Salary,position as Position;
end loop;
close cur1;
end //

call getemp_position;

create table empcount(ecount int not null default 0);
insert into empcount values(0);
select * from empcount;
select count(*) from employees;

delimiter //
create trigger insertempcount
after insert on employees
for each row
begin
update empcount set ecount=(select count(employee_id) from employees);
end //

insert into employees values(1000,'komal','shah','k@gmail.com',76796,now(),'AD_VP',5000,null,101,60);
select * from empcount;
select count(*) from employees;

delimiter //
create trigger deleteempcount
after delete on employees
for each row
begin
update empcount set ecount=(select count(employee_id) from employees);
end //

delete from employees where employee_id=1000;
select * from empcount;
select count(*) from employees;
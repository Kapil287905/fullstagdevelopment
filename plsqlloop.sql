use amazon;
-- if else block conditonal block
-- write procedure to check person is elegible to vote or not
delimiter //
create procedure checkage(in age int)
begin
if age>=18 then
select 'eligible to vote';
else
select 'not eligible to vote';
end if;
end // 
call checkage(45);
call checkage(5);

-- find greast number among any of threed number
delimiter //
create procedure greastestnumber(in a int,in b int,in c int)
begin
if a>b and a>c then
select 'a is grater';
elseif b>c then
select 'a is grater';
else
select 'c is grater';
end if;
end // 
call greastestnumber(45,35,55);
call greastestnumber(55,35,45);
call greastestnumber(55,65,45);

drop procedure greastestnumber;

delimiter //
create procedure greastestnumber(in a int,in b int,in c int)
begin
if a>b and a>c then
select 'a is greastest number';
elseif b>c then
select 'b is greastest number';
else
select 'c is greastest number';
end if;
end // 
call greastestnumber(45,35,55);
call greastestnumber(55,35,45);
call greastestnumber(55,65,45);

-- write a procedure to show emp max salary when it id greater then 10K and show min salary when 
-- it is less than 10k
delimiter //
create procedure checkalary(in sal float)
begin
if sal>10000 then
select * from emp where salary in(select max(salary) from emp);
else
select * from emp where salary in(select min(salary) from emp);
end if;
end //
call checkalary(5000); -- showing min salaried emp details
call checkalary(15000); -- showing max salaried emp details

use hr;
delimiter //
create procedure get_employee()
begin
select e.first_name,e.last_name,d.department_name 
from employees e inner join departments d  on e.department_id=d.department_id;
end //
call get_employee;

delimiter //
create procedure getlimitedemployee(in n int)
begin
select first_name,last_name,salary,hire_date from employees limit n;
end //
call getlimitedemployee(5);
call getlimitedemployee(10);

delimiter //
create procedure countemployee()
begin
select count(*) as total_emp from employees;
end //
call countemployee;

drop procedure countemployee;

delimiter //
create procedure countemployee()
begin
select count(*) as total_employees from employees;
end //
call countemployee;

delimiter //
create procedure countemployeed(out totalcount int)
begin
select count(*) as total_employees into totalcount from employees;
end //
set @totalcount=0;
call countemployeed(@totalcount);
select @totalcount as TotalEmployee;
select @totalcount+10 as "Total Employee";

drop procedure countemployeed;

-- looping (countinous start to perform repeatation untill conditein get false)
-- three parameter (start,condition,increment/decrement)
-- 1) while loop
delimiter //
create procedure whiledemo()
begin
declare i int default 1;
while i<=5 do
select i;
set i=i+1;
end while;
end //

call whiledemo;
 
 use hr;
drop procedure whiledemo;

delimiter //
create procedure whiledemo()
begin
declare i int default 1;
declare output varchar(20) default '';
while i<=5 do
set output=concat(output,i,'');
-- select i;
set i=i+1;
end while;
select output;
end //

call whiledemo;

drop procedure whiledemo;

-- 2) repeat loop or until loop
delimiter //
create procedure repeatloop()
begin
declare i int;
declare output varchar(20);
set i=1;
set output="";
repeat
set output=concat(output,i,' ');
set i=i+1;
until i>5 end repeat;
select output;
end //

call repeatloop;

-- lable loop
delimiter //
create procedure lableloop()
begin
declare i int default 1;
declare output varchar(20) default "";
go:loop
if i>5 then leave go;
end if;
set output=concat(output,i,' ');
set i=i+1;
iterate go;
end loop;
select output;
end //

call lableloop;

drop procedure lableloop;



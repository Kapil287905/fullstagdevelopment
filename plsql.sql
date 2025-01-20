use amazon;
-- syntax for procedures

delimiter //
-- create procedure proc_name(in,out,inout,optional)
-- begin
-- select start;
-- end //

-- call proc_name(optional)

-- deop procedure proc_name;

select "wellcome";


-- write a procedure to show all employee detail

delimiter //
create procedure showemp()
begin
select * from emp;
end//

call showemp;

drop procedure showemp;

delimiter $
create procedure showemp()
begin
select eid,ename from emp;
end $

call showemp;

-- use of procedure parameter (in,out,inout)
-- input parameter to take input from user

-- writer a procedure to dhow entered employee detail as per name.

delimiter #
create procedure show_given_empdetails(in empname char(20)) -- parameter
begin
select * from emp where ename=empname;
end #

call show_given_empdetails('pooja');
call show_given_empdetails('keerti'); -- argument

-- write procedure to show arithmatic operation by taking number from user

delimiter #
create procedure calculator(in a int,b int,out addition int)
begin
set addition=a+b;
select addition;
end #

call calculator(5,6,@addition);

--

delimiter $
create procedure sub1(in a int,b int,out sub int)
begin
set sub=a-b;
end $

call sub1(5,6,@sub);
select @sub;

call sub1(11245,60,@sub);
select @sub;

delimiter //
create procedure cal(in x int,in y int,out add1 int,out sub int,out mul int,out div1 int,out mod1 int)
begin
set add1=x+y;
set sub=x-y;
set div1=x/y;
set mul=x*y;
set mod1=x%y;
end //

call cal(3,4,@add1,@sub,@mul,@div1,@mod1);
select @add1,@sub,@mul,@div1,@mod1;

-- write a procedure to show emp salary whose id is entered by user

delimiter //
create procedure showsalary(in id int,out sal decimal(8,2))
begin
select salary from emp where eid=id;
end //

call showsalary(1,@sal);
-- call showsalary; -- error required input argument

-- inout paramater
-- write procuder to show count of emplouee

delimiter $
create procedure empcount(inout count1 int)
begin
select count(eid) from emp;
end $

call empcount(@count1);

delimiter $
create procedure empcountsal(inout count2 int)
begin
select count(eid) from emp where salary>count2;
end $
set @count2=50000;
call empcountsal(@count2);

-- write proceduer to find employee count ask by gender value
delimiter //
create procedure empcountgender(inout countgender varchar(20))
begin
select count(eid) from emp where gender=countgender;
end //

drop procedure empcountgender;

delimiter //
create procedure empcountgender(inout countgender varchar(20))
begin
select count(eid) from emp where gender=countgender;
end //
set @countgender="male";
call empcountgender(@countgender);

set @countgender="female";
call empcountgender(@countgender);

use amazon;
select * from emp;

-- Date function

select now(); -- date & time
select sysdate(); -- date & time
select curdate(); -- date
select current_date(); -- date
select current_time(); -- time
select current_timestamp();  -- date & time

select * from emp;
insert into emp values(16,'harry','male','8678678','h@gmail.com','delhi',curdate(),40000,'India');

select day('2020-03-21');
select day(now());

-- WQ to show whose birthday on 15th day of every mont
select * from emp where day(dob)=15;

select dayname('2020-03-21');
select dayname(now());

select dayofmonth('2020-03-21');
select dayofmonth(now());

select dayofweek('2020-03-21');
select dayofweek(now()); -- sunsay as 1 and show number as per dayname

select dayofyear('2020-03-21'); -- 1st jan as 1day and respectively showing day count
select dayofyear(now());

select month('2020-03-21'); 
select month(now());

select monthname('2020-03-21'); 
select monthname(now());

-- WQ to emp whose birthday on this mont
select * from emp where month(dob)=1;
-- or
select * from emp where monthname(dob)='january';
-- or
select * from emp where month(dob)=month(now());

select year('2020-03-21');
select year(now());

select yearweek('2020-03-21');
select yearweek(now()); -- zero is 1st week

-- WQ to show age as per emp birthday
select dob,year(now())-year(dob) as age from emp;

-- To store age data we create view
create view emp_age as select eid,ename,dob,year(now())-year(dob) as age from emp;
select * from emp_age;

-- WQ to display all emp detais who are turning up to age of 25
select dob,year(now())-year(dob) as age from emp where year(now())-year(dob)=24;

select week('2020-03-21');
select week(now());  -- zero is 1st week

select weekofyear('2020-03-21');
select weekofyear(now());  -- one is 1st week

select adddate('2020-03-21',5);
select adddate(now(),5);

select date_add('2020-03-21',interval 10 day);
select date_add(now(),interval 10 day);

select date_add('2020-03-21',interval 10 month);
select date_add(now(),interval 10 month);

select date_add('2020-03-21',interval 10 year);
select date_add(now(),interval 10 year);

select date_sub('2020-03-21',interval 10 day);
select date_sub(now(),interval 10 day);

select date_sub('2020-03-21',interval 10 month);
select date_sub(now(),interval 10 month);

select date_sub('2020-03-21',interval 10 year);
select date_sub(now(),interval 10 year);

select datediff('2020-03-21',now()); -- wrong show in negative number
select datediff(now(),'2020-03-21');

-- date formating
select date_format('2020-03-21','%D %M %Y');

select dob,date_format(dob,'%D %M %Y') from emp;

select date_format('2020-03-21','%d-%m-%y');
select date_format(now(),'%d-%m-%y %T');

select time(now());
select hour(now());
select minute(now());
select second(now());

-- WQ to display emp whose birth on next week
select eid,dob from emp where week(dob)=week(now())+1; 
-- WQ to display emp whose birth on next month
select eid,dob from emp where month(dob)=month(now())+1;

-- WQ to show total salary of male emp and show count of male emp 
select gender,count(eid),sum(salary) from emp where gender='male' group by gender;



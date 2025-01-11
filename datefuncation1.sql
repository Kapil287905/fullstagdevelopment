use amazon;
select * from emp;

-- WQ to display employee whose bairthday on same day(dayname) in next week
select dayname(dob) from emp;

select eid,ename,dob,dayname(dob) from emp where dayname(now())=dayname(dob) and week(dob)=week(now())+1;

-- string function (string is an set of literals enclose within quotes)
select char_length('SQL');
select character_length('SQL');
select length('SQL');
select char_length('SQLis backend language');
select char_length(123465);
select char_length(65.787);

-- WQ to show total digit of salary from emp table
select salary,length(round(salary)) from emp;

-- WQ to show emp whose email total length less than 10;
select eid,email,ename,length(email) from emp where length(email)<10;

select concat('SQL',' ','nosql');
select concat(eid,'-',ename) as 'ID-Name' from emp;

select upper('hello');
select lower('hello');

select eid,upper(ename) as Name from emp;

select ucase('hello');
select lcase('hello');

select reverse('SQL');
select reverse(7340);

select replace('welcome to sql','e','z'); -- follows case(uppper and lower)

select * from emp;
-- WQ to show emp id,name and city in abbrevayed from 
-- (i.e mimbai can be MU,delhi can be DH,pune can be PU,gujrat can be GJ,banglore can be BA)
select eid,ename,replace(city,'mumbai','MU') from emp;


select eid,ename,
case
when city='mumbai,delhi' then replace(lower(city),'mumbai,delhi','MU,DH')
when city='mumbai' then replace(lower(city),'mumbai','MU')
when city='delhi' then replace(lower(city),'delhi','DH')
when city='pune' then replace(lower(city),'pune','PU')
when city='gujrat' then replace(lower(city),'gujrat','GJ')
when city='banglore' then replace(lower(city),'banglore','BA')
else city
end 'city code'
from emp;

select left('good morning',6); -- from left side after 6 position it truncate the string
select left('helio',2);
select left('helio',23);
select left(123456,2);

select right('good morning',6); -- from right side after 6 position it truncate the string

select lpad('SQL',10,'No');
select lpad('SQL',10,'#'); -- from left side adds # until given dtring size up to 10

select rpad('SQL',10,'#'); -- from right side adds # until given dtring size up to 10

select lpad(eid,5,'IT-'),ename from emp;

select substring('Welcome',5); -- start from given position number as 5 to end string but it truncate before char
select substring('Welcome',2); -- elcome
select substring('Welcome',2,5); -- elcom (start=2 and count from that 1 to 5)

select insert('welcome',2,5,'good'); -- wgoode
select insert('welcome',2,4,'good'); -- wgoodme
select insert('hi',2,2,'good'); -- hgood

-- joins (use to fetch result from more than one table)
select * from students; -- 4*6
select * from projects; -- 1*5

select * from students,projects; -- 4*11 (row multies and colums added)

select * from emp; -- 15*9
select * from customers; -- 14*9
select* from emp,customers;

-- type of joins
-- 1) inner join
-- 2) outer join
-- 3) natural join
-- 4) cross join
-- 5 self join
-- and other equi and Non-eaui join


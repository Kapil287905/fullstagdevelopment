use amazon;
select database();

show tables;
select * from customers;
desc customers;

create table student
(
sid int,
name char(20),
gender enum('male','female','other'),
dob date,
city char(50),
totalmarks int
);

create table students
(
sid int,
name char(20),
gender enum('male','female','other'),
dob date,
city char(50),
totalmarks int
);

desc students;

insert into students value('101','komal','female','2000-06-12','mumbai',400);
insert into students value(null,'kk','male','2001-06-12','mumbai',400);
select * from students;

update students set sid=102 where name="kk";
alter table students modify sid int not null;

insert into students value(null,'aaaa','male','2005-06-12','dheli',200);

desc students;

-- wq to apply not null to name,gender colum
alter table students modify sid int not null;
update students set gender="female" where sid=101;

select * from students;

alter table students modify gender enum('male','female','other') not null;

alter table students modify name char(20) not null;

-- default
alter table students modify name char(20);
desc students;

insert into students value(105,'rohit','','2005-06-12','dheli',270);

-- default
desc students;

insert into students(sid,gender) value(106,'male');
select * from students;

-- WQ to default value from city as "none"
alter table students modify city char(50) default 'none';

insert into students(sid,gender) value(107,'female');

-- WQ to default value from city as null
alter table students modify city char(50);
-- or
alter table students modify city char(50) default null;
insert into students(sid,gender) value(108,'female');

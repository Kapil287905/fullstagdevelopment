use amazon;
show tables;
select * from students;
desc students;

-- check constraint
-- WQ to and check constraint for totalmarks i.e totalmarks>=0 and totalmarks<=500
alter table students modify totalmarks int check(totalmarks>=0 and totalmarks<=500);
desc students;
show create table students; -- show all constraint

insert into students value(108,'neeta','female','2000-09-09','pune',943); -- error for check
update students set totalmarks=900 where sid=101;  -- error for check 

-- to remove check constraint
alter table students modify totalmarks int;
-- or
alter table students drop constraint student_chk_1;

-- Key constraint (unique,primary,foreing)
-- unique(non-repeated nut allow null)
select * from students;
desc students;

delete from students where sid=101;
insert into students value('101','meena','female',null,null,null); -- error for unique

alter table students modify sid int;

alter table students modify sid int unique;
insert into students value(null,'meena','female',null,null,null);
insert into students value(null,'roshan','male',null,null,null);

select * from students;
alter table students modify sid int; -- can't remove unique key;
desc students;
show create table students;
show index from students;

alter table students drop constraint sid;
desc students;
show create table students;
show index from students;


-- primary key (unique(no duplication) without not null)
-- add primary key to sid
delete from students where sid is null;
alter table students modify sid int unique not null;

alter table students drop constraint sid_2;
alter table students modify sid int;
alter table students drop constraint sid;

desc students;

-- alter table student modify sid int primary key;
-- or
alter table students add primary key(sid);
desc students;
show create table students;
show index from students;

-- insert into students value(null,'hina','female',null,null,null); --error because primary key
-- insert into students value(101,'hina','female',null,null,null); --error because primary key

alter table students drop primary key;
desc students;
show create table students;
show index from students;
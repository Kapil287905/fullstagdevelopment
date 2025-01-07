use amazon;
select database();
show tables;
select * from students;
-- creating foreign key tabe as projects has sid,pid,title,frontend,backend
-- foreign key (reference key which nothing but as primary key of another table)
desc students;
alter table students add primary key(sid);
create table projects
(
pid int primary key,
sid int,
title varchar(50),
frontend varchar(50),
backend varchar(50),
foreign key(sid) references students(sid)
);
desc projects;
show create table projects;
show index from projects;

create table mentor
(
mid int primary key,
name char(50),
deptname char(50),
sid int,
pid int
);

desc mentor;
alter table mentor add foreign key(sid) references students(sid);
desc mentor;
alter table mentor add foreign key(pid) references projects(pid);
desc mentor;

select * from students;
insert into projects values(1000,102,'Hotel system','js','mysql');
insert into projects values(1001,null,'chatbot','python',null);
select * from projects;
insert into projects values(1002,102,'portfolio','reactjs','express');

insert into mentor values(1,'raju','It',102,1000);
insert into mentor values(2,'pooja','cs',105,1001);
insert into mentor values(3,'usha','cs',108,1002);
select * from mentor;

-- deleteing fk row
delete from mentor where mid=1; 
select * from mentor;
select * from students;

-- delete from projects where pid=1001; -- error mentor table not allowing
-- delete from students where sid=102; -- error projects table not allowing

-- to apply new rule of foreign key with cascade 1st remove old FK constraint
show create table projects;
alter table projects drop constraint projects_ibfk_1;
alter table projects drop index sid;
desc projects;

show create table mentor;
alter table mentor drop constraint mentor_ibfk_1;
alter table mentor drop constraint mentor_ibfk_2;
alter table mentor drop index sid;
alter table mentor drop index pid;
desc mentor;


alter table projects add foreign key(sid) references students(sid) on delete cascade;
show create table projects;

delete from students where sid=102;
select * from projects;

alter table mentor add foreign key(sid) references students(sid) on delete set null;
select * from mentor;
show create table mentor;
delete from students where sid=105;
select * from mentor;




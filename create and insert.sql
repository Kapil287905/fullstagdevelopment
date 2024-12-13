--- syntax create db
---- create database database_name
create database db1;
show databases;
create database db2;
show databases;
use db1;
-- use db29; -- unknowm db
select database();
show tables;

-- create tables
-- ligin(username,password)

create table login
(
username varchar(30),
password varchar(50)
);

show tables;
describe login;
desc login;

select * from login;
insert into login value("komal","1234");
select * from login;
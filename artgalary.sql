create database Artgallary;
use Artgallary;
create table artists
(
 art_id int primary key,
 first_name varchar(20),
 last_name varchar(20)
);
desc artists;
select * from artists;

insert into artists values(1,"Thomas","Black"),(2,"Kate","Smith"),(3,"Natali","Wein"),(4,"Francesco","Benelli");
select * from artists;

create table collectors
(
 id int primary key,
 first_name varchar(20),
 last_name varchar(20)
);
desc collectors;
select * from collectors;

insert into collectors values(101,"Brandon","Cooper"),(102,"Laura","Fisher"),(103,"Chirstina","Buffet"),(104,"Steve","Stevenson");
select * from collectors;

create table painting
(
 paint_id int primary key,
 fname varchar(20),
 artist_id int,
 listed_price int,
 foreign key(artist_id) references artists(art_id)
);
desc painting;
select * from painting;

insert into painting values(11,"Miracle",1,300.00),(12,"Sunshine",1,700.00),(13,"Pretty woman",2,2800.00),(14,"Handsome man",2,2300.00),(15,"Barbie",3,250.00),(16,"Cool painting",3,5000.00),(17,"Black square #1000",3,50.00),(18,"Mountains",4,1300.00);
select * from painting;

create table sales
(
 sales_id int primary key,
 date date, 
 painting_id int,
 artist_id int,
 collector_id int,
 sales_price int,
 foreign key(artist_id) references artists(art_id),
 foreign key(collector_id) references collectors(id),
 foreign key(painting_id) references painting(paint_id)
);
desc sales;
select * from sales;

insert into sales values(1001,"2021-11-01",13,2,104,2500.00),(1002,"2021-11-10",14,2,102,2300.00),(1003,"2021-11-10",11,1,102,300.00),(1004,"2021-11-15",16,3,103,4000.00),(1005,"2021-11-22",15,3,103,200.00),(1006,"2021-11-22",17,3,103,50.00);
select * from sales;

-- 01) We want to list paintings that are priced higher than the average.
select avg(listed_price) from painting;
select * from painting where listed_price > (select avg(listed_price) from painting);

-- 02) we want to list all collectors who purchased paintings from our gallery.
select distinct c.first_name from collectors c join sales s on c.id=s.collector_id; 

-- 03) we want to see the total amount of sales for each artist who has sold at least one
-- painting in our gallery.
select a.first_name,sum(s.sales_price) as total_price from artists a join sales s on a.art_id=s.artist_id GROUP BY a.first_name having SUM(s.sales_price) > 0;

-- 04) we want to calculate the number of paintings purchased through our gallery.
select count(*) from sales s join painting p on s.painting_id=p.paint_id;

-- 05) we want to show the first names and the last names of the artists who had zero
-- sales with our gallery.
select a.first_name,a.last_name from artists a left join sales s on s.artist_id = a.art_id where s.sales_id is null;

-- 06) Find painting name who has lowest listing price.
select fname from painting where listed_price = (select min(listed_price) from painting);

-- 07) Find painting id whose sales happens between 1st nov 2021 to 15th nov 2021.
select painting_id from sales where date between '2021-11-01' and '2021-11-15';

-- 08) Show painting details whose name ends with 'n'
select * from painting where fname like '%n';

-- 09) Display collectors id whose name is 'Laura'
select id from collectors where first_name='Laura';

-- 10) Find sales details of artists whose id is 2
select * from sales where artist_id=2;

-- 11) Find count of sales happens for collector id 103.
select count(*) as countofsales from sales where collector_id=103;

-- 12) update artists name of artists id 3 set first name as 'zika'
update artists set first_name='Zika' where art_id=3;
select * from artists;

-- 13) Change column name of collectors set first_name to fname and last_name to lname.
alter table collectors rename column first_name to fname;
desc collectors;
alter table collectors rename column last_name to lname;
desc collectors;

-- 14) Delete painting details whose id is 18
delete from painting where paint_id=18;
select * from painting;

-- 15) detele complete data of sales.
truncate table sales;
select * from sales;

select user();
select current_user();

select user from mysql.user; -- lost all user account

create user 'kapil'@'localhost' identified by 'qwerty@123';

show grants for 'kapil'@'localhost';
show grants for 'root'@'localhost';

grant all privileges on *.* to 'kapil'@'localhost';
show grants for 'kapil'@'localhost';
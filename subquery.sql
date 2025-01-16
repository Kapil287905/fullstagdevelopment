use collegedb;
select * from studentnew;
select * from marksnew;

-- sub query q2 oberator (q1);
-- Q2) find student whose marks are grater then min marks of any student;
select min(totalmarks) from marksnew;
select s.studentid,s.name,m.totalmarks from studentnew s,marksnew m where s.studentid=m.studentid and totalmarks>(select min(totalmarks) from marksnew);

-- Q3) find student whose totalmarks are sililar then average of all student.
select avg(totalmarks) from marksnew;
select s.studentid,s.name,m.totalmarks from studentnew s,marksnew m where s.studentid=m.studentid and totalmarks=(select avg(totalmarks) from marksnew); -- result only 1 row
-- or 
select s.studentid,s.name,m.totalmarks from studentnew s,marksnew m where s.studentid=m.studentid and totalmarks in(select avg(totalmarks) from marksnew); -- result many row

-- Q4) find student whose totalmarks is within the range od smallest marks and 85
select s.studentid,s.name,m.totalmarks from studentnew s,marksnew m where s.studentid=m.studentid and m.totalmarks between (select min(totalmarks) from marksnew) and 85;

-- Q5) find student whose totalmatks are present
select s.studentid,s.name,m.totalmarks from studentnew s,marksnew m where s.studentid=m.studentid and m.totalmarks is not null;
-- or 
select s.studentid,s.name,m.totalmarks from studentnew s right join marksnew m on s.studentid=m.studentid and m.totalmarks is not null;

-- Q6) find student whose record is not present in marks table
select * from studentnew;
select * from marksnew;

select * from studentnew where studentid not in (select studentid from marksnew);
-- or
select * from studentnew where not exists (select studentid from marksnew where studentnew.studentid=marksnew.studentid);

select s.studentid,s.name from studentnew s left join marksnew m on s.studentid!=m.studentid; -- wrong answer

-- Q7) find student whose marks are not assigned
select s.studentid,s.name from studentnew s,marksnew m where s.studentid=m.studentid and m.totalmarks is null
union
select * from studentnew where studentid not in (select studentid from marksnew);


use hr;
show tables;
select * from regions;
select count(*) from regions; -- 4
select * from countries; -- 25
select * from locations; -- 23
select * from departments; -- 27
select * from employees; -- 107
select * from jobs; -- 19
select * from job_history; -- 10

-- Write a query to display the name (first and last ) for those employees who gets more 
-- salary than the employee whose ID is 163.

select salary from employees where employee_id=163;
select * from employees where salary>9500;
select first_name,last_name,salary from employees where salary>(select salary from employees where employee_id=163);

-- Write a query to display all the information of employess whose salary is within the 
-- range of smallest salary and 2500.
select min(salary) from employees;
select * from employees where salary between (select min(salary) from employees) and 2500;

-- Write a query to display the name (first and last ),salary,department id,job id 
-- for those employees who works in the same designation as the employee works whose id is 169.
select job_id from employees where employee_id=169;
select first_name,last_name,salary,department_id,job_id from employees where job_id=(select job_id from employees where employee_id=169);
-- or
select first_name,last_name,salary,department_id,job_id from employees where job_id in(select job_id from employees where employee_id=169);

-- Write a query to display the name (first and last ),salary,department id,job id for 
-- those employees who earn such amount of salary which is the smallest salary of any of the departments.
select first_name,last_name,salary,department_id,job_id from employees where salary=(select min(salary) from employees);
-- or
select first_name,last_name,salary,department_id,job_id from employees where salary in(select min(salary) from employees);
-- or
select first_name,last_name,salary,department_id,job_id from employees where salary =any(select min(salary) from employees);

select department_id,count(employee_id),min(salary) from employees group by department_id;
select department_id,salary from employees where department_id=20;

-- Write a query to get the details of employees who are managers.
select * from employees where employee_id in (select manager_id from employees);

-- Write a query to get the details of employees who manage a department.
select * from employees where employee_id in (select manager_id from employees);

-- Write a query to display the department id and the total salary for those departments which contains at least one employee
select department_id,count(employee_id),sum(salary) from employees where department_id is not null group by department_id having count(employee_id)>=1;

-- Write a query to display the name (first and last ) and department for all employees for any existence of 
-- those employees whose salary is more than 3700. 
select first_name,last_name,salary,department_id from employees where salary>3700 and department_id is not null;

select e.first_name,e.last_name,e.salary,e.department_id,d.department_name 
from employees e,departments d 
where e.department_id=d.department_id and e.salary>3700;

-- Write a query to display all the information of those employees who 
-- did not have any job in the past.
select distinct(employee_id) from job_history;

select * from employees where employee_id not in ( select employee_id from job_history);

-- Write a query to display employee name(firstname,lastname),employee_id and job title for all employees whose location is Toronto
select * from locations where city='Toronto';
select e.employee_id,e.first_name,e.last_name,j.job_title,l.city from employees e,departments d,jobs j,locations l 
where e.department_id=d.department_id and j.job_id=e.job_id and d.location_id=l.location_id and l.city='Toronto';



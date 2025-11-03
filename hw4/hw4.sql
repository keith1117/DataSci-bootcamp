-- 1050
select actor_id,director_id 
from ActorDirector 
group by actor_id,director_id 
having count(actor_id) >= 3 and count(director_id) >= 3;

-- 1667
select user_id, concat(upper(left(name,1)),lower(right(name,length(name)-1))) as name
from Users 
order by user_id

-- 175
select Person.FirstName, Person.LastName, Address.City, Address.State 
from Person 
left join Address on Person.PersonId = Address.PersonId;

-- 176
select max(a.Salary) as SecondHighestSalary
from Employee a
join Employee b on a.Salary < b.Salary

-- 1327
select p.product_name, sum(o.unit) as unit
from Products as p
join Orders as o on p.product_id = o.product_id
where o.order_date >= '2020-02-01' and o.order_date < '2020-03-01'
group by p.product_id, p.product_name
having sum(o.unit) >= 100;

-- 1378
select b.unique_id, a.name 
from employees a
left join employeeuni b
on a.id = b.id;

-- 550
select round(count(distinct player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from Activity
where (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) in (select player_id, MIN(event_date) as first_login from Activity group by player_id)

-- 1075
select p.project_id, round(avg(e.experience_years),2) as average_years
from Project p
left join Employee e on p.employee_id=e.employee_id
group by p.project_id

-- 185
select d.name as Department, e.name as Employee, e.salary as Salary 
from Employee e 
join Department d on e.departmentId = d.id 
where (select COUNT(distinct salary)
       from Employee e2
       where e2.departmentId = e.departmentId and e2.salary >= e.salary) <= 3
order by Department, Salary desc;

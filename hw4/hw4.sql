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

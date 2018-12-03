# Write your MySQL query statement below
select E.name as "Employee"
from Employee E, Employee H
where E.ManagerId= H.Id and E.Salary> H.Salary


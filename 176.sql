# Write your MySQL query statement below

select IFNULL (
	(select Salary 
	from Employee
	group by Salary
	order by Salary DESC
	limit 1,1),null
) as SecondHighestSalary

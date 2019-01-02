# Write your MySQL query statement below
select t.Id from Weather t,Weather y where t.RecordDate = DATE_ADD(y.RecordDate,INTERVAL 1 DAY ) and t.Temperature > y.Temperature

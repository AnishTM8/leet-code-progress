-- Last updated: 3/18/2026, 9:04:13 PM
# Write your MySQL query statement below
SELECT Employee.name, Bonus.bonus FROM Employee LEFT JOIN Bonus
ON Employee.empId = Bonus.empID 
WHERE bonus < 1000 OR bonus IS NULL;

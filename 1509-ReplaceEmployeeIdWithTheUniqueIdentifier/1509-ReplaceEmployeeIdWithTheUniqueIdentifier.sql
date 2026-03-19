-- Last updated: 3/18/2026, 9:03:58 PM
# Write your MySQL query statement below
SELECT eu.unique_id, e.name FROM Employees e
LEFT JOIN EmployeeUNI eu
ON eu.id = e.id
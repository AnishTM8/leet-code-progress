-- Last updated: 3/18/2026, 9:04:02 PM
# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price FROM Product p
Inner JOIN Sales s
ON p.product_id = s.product_id
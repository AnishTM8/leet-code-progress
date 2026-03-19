-- Last updated: 3/18/2026, 9:03:53 PM
# Write your MySQL query statement below
SELECT a.machine_id, round(avg(b.timestamp - a.timestamp), 3) as processing_time 
FROM Activity a, Activity b
WHERE a.machine_id = b.machine_id AND a.process_id = b.process_id 
AND a.activity_type = 'start' and b.activity_type = 'end'
GROUP BY machine_id
-- Import in hbtn_0c_0 database this table
SELECT city, AVG(values) AS avg_temp FROM temperatures WHERE month=7 or month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

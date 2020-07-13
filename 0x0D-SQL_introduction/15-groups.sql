--script que enumere la cantidad de registros
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;

--script que enumere la cantidad de registros
SELECT score, count(*) AS number FROM second_table GROUP BY score DESC;

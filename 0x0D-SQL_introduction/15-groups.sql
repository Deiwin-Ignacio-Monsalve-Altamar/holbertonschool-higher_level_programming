--script que enumere la cantidad de registros
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;

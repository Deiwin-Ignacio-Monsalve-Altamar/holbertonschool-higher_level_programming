--script que enumere la cantidad de registros con la misma puntuación en la tabla
SELECT score, count(*) AS number FROM second_table GROUP BY score DESC;

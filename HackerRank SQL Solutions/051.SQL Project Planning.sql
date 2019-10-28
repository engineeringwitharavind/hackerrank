SELECT start_date, MIN(end_date)
FROM 
    (SELECT start_date FROM PROJECTS WHERE start_date NOT IN (SELECT end_date FROM PROJECTS)) a,
    (SELECT end_date FROM PROJECTS WHERE end_date NOT IN (SELECT start_date FROM PROJECTS)) b
where start_date < end_date
GROUP BY start_date
ORDER BY datediff(day, start_date, MIN(end_date)), start_date;
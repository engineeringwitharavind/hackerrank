/* REvising the Select Query-I */
SELECT *
FROM CITY
WHERE
    COUNTRYCODE = 'USA'
    AND POPULATION > 100000;

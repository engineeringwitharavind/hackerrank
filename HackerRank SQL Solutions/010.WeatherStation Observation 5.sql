--MYSQL Solution--

SELECT CITY,char_LENGTH(CITY) 
FROM STATION 
ORDER BY LENGTH(CITY), CITY ASC LIMIT 1; 
SELECT CITY,char_LENGTH(CITY) 
FROM STATION 
ORDER BY LENGTH(CITY) DESC, CITY DESC LIMIT 1;
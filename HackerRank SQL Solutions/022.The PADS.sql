SELECT CONCAT(NAME, 
              CASE WHEN occupation = "Professor" THEN "(P)"
                   WHEN occupation = "Actor" THEN "(A)" 
                   WHEN occupation = "Doctor" THEN "(D)" 
                   WHEN occupation = "Singer" THEN "(S)" 
              END )
FROM OCCUPATIONS 
ORDER BY NAME; 

SELECT "There are a total of", COUNT(OCCUPATION), CONCAT(LOWER(OCCUPATION),"s.") 
FROM OCCUPATIONS 
GROUP BY OCCUPATION 
ORDER BY COUNT(OCCUPATION) ASC, OCCUPATION ASC;

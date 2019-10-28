SELECT H.hacker_id ,H.name ,COUNT(*) --AS TOTAL
FROM Hackers AS H 
LEFT JOIN Challenges AS C 
ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING COUNT(*) = (SELECT TOP 1 COUNT(*) 
                  FROM CHALLENGES 
                  GROUP BY hacker_id 
                  ORDER BY COUNT(*) DESC ) 
                  OR COUNT(*) IN ( SELECT TOTAL FROM 
                                                    ( SELECT COUNT(*) AS TOTAL 
                                                      FROM HACKERS H, CHALLENGES C 
                                                      WHERE H.hacker_id = C.hacker_id 
                                                      GROUP BY H.hacker_id, H.name ) AS COUNTS                                        
								   GROUP BY TOTAL HAVING COUNT(*) = 1 )
ORDER BY COUNT(*) DESC, H.hacker_id;
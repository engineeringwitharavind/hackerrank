SELECT (CASE g.grade >= 8 WHEN TRUE THEN s.name ELSE null END),g.grade,s.marks 
FROM students s 
INNER JOIN grades g 
ON s.marks BETWEEN min_mark AND max_mark 
ORDER BY g.grade DESC,s.name,s.marks;
SELECT  con.contest_id,
        con.hacker_id, 
        con.name, 
        sum(total_submissions), 
        sum(total_accepted_submissions), 
        sum(total_views), sum(total_unique_views)
FROM CONTESTS AS con 
JOIN COLLEGES AS col 
ON con.contest_id = col.contest_id 
JOIN CHALLENGES AS cha 
ON  col.college_id = cha.college_id 
LEFT JOIN
    (SELECT challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views
FROM view_stats 
GROUP BY challenge_id) vs 
ON cha.challenge_id = vs.challenge_id 
LEFT JOIN
    (SELECT challenge_id, sum(total_submissions) as total_submissions, 
	 sum(total_accepted_submissions) as total_accepted_submissions 
     FROM submission_stats 
     GROUP BY challenge_id) ss 
ON cha.challenge_id = ss.challenge_id
        GROUP BY con.contest_id, con.hacker_id, con.name
        HAVING sum(total_submissions)!=0 or 
                sum(total_accepted_submissions)!=0 or
                sum(total_views)!=0 or
                sum(total_unique_views)!=0
        ORDER BY contest_id;
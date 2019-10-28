SELECT Q2.submission_date, Q3.unique_count, Q2.hacker_id, H.name FROM
/**Using sliding window to take the top hacker based on the orders given in each sub group**/
    (
        SELECT submission_date, submission_count, hacker_id, 
        RANK() OVER (PARTITION BY submission_date ORDER BY submission_count DESC, hacker_id ASC) Rank
        FROM
        (
            SELECT submission_date, COUNT(submission_date) as submission_count, hacker_id
            FROM Submissions
            GROUP BY submission_date, hacker_id
        ) Q1
    ) Q2
    JOIN 
    (
        --using sliding window and day(date) to check wether or not the submissions of the hacker is the same number of the day till that day
        SELECT submission_date, COUNT(DISTINCT hacker_id) unique_count FROM
            (
            SELECT DISTINCT(T0.hacker_id), T0.submission_date, 
            COUNT(T0.submission_date) OVER(PARTITION BY T0.hacker_id ORDER BY T0.submission_date ASC) subdate_count
            FROM 
                    /** since we only need 1 submission in each day to count the hacker,I group by the hacker to find distinct hackers in each day. 
					If We take the whole submissions table without the group by we will miscalculate unique hackers, because we are counting hackers 
					submission till that specific day so I will count hacker X in day 5 if that hacker have 5 submissions or more in day 5, but the 
					problem here is we miss the fact that maybe hacker X made all 5 submissions on the day 5, so it is needed to just take one submission 
					per day for each hacker using a simple group by function **/
                (
                    SELECT submission_date, hacker_id 
                    FROM Submissions 
                    GROUP BY submission_date, hacker_id
                )T0
            ) T1 
        WHERE T1.subdate_count >= DAY(T1.submission_date)
        GROUP BY submission_date 
    ) Q3
    ON Q3.submission_date= Q2.submission_date
    JOIN Hackers H ON H.hacker_id=Q2.hacker_id
    WHERE Q2.Rank = 1;
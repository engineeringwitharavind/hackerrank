SELECT C.COMPANY_CODE, 
       C.FOUNDER, 
       COUNT(DISTINCT L.LEAD_MANAGER_CODE), 
       COUNT(DISTINCT S.SENIOR_MANAGER_CODE), 
       COUNT(DISTINCT M.MANAGER_CODE),
       COUNT(DISTINCT E.EMPLOYEE_CODE) 
FROM COMPANY C, LEAD_MANAGER L, SENIOR_MANAGER S, MANAGER M, EMPLOYEE E 
WHERE C.COMPANY_CODE = L.COMPANY_CODE 
  AND L.LEAD_MANAGER_CODE = S.LEAD_MANAGER_CODE 
  AND S.SENIOR_MANAGER_CODE = M.SENIOR_MANAGER_CODE 
  AND M.MANAGER_CODE = E.MANAGER_CODE 
GROUP BY C.COMPANY_CODE, C.FOUNDER  
ORDER BY C.COMPANY_CODE;
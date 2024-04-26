# SELECT 
#     CASE
#         WHEN MONTH(DIFFERENTIATION_DATE) IN (1, 2, 3) THEN '1Q'
#         WHEN MONTH(DIFFERENTIATION_DATE) IN (4, 5, 6) THEN '2Q'
#         WHEN MONTH(DIFFERENTIATION_DATE) IN (7, 8, 9) THEN '3Q'
#         ELSE '4Q'
#     END AS QUARTER,
#     COUNT(ID) AS ECOLI_COUNT
# FROM ECOLI_DATA
# GROUP BY QUARTER
# ORDER BY QUARTER ASC;

SELECT 
    CASE
        WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 1 AND 3 THEN '1Q'
        WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 4 AND 6 THEN '2Q'
        WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 7 AND 9 THEN '3Q'
        ELSE '4Q'
    END AS QUARTER,
    COUNT(ID) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER ASC;
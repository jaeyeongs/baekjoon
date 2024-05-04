SELECT
  ROUND(AVG(sum_bill), 2) AS avg_sales
FROM
  (SELECT 
    day,
    SUM(total_bill) AS sum_bill
  FROM 
    tips
  GROUP BY
    day
  )

SELECT
  *
FROM
  tips
WHERE
  total_bill IN (
    SELECT
      total_bill
    FROM
      tips
    GROUP BY
      day
    HAVING
      MAX(total_bill)
  )

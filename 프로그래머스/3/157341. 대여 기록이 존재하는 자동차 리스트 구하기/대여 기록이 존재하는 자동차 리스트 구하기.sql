SELECT DISTINCT(CAR_ID) AS CAR_ID
FROM CAR_RENTAL_COMPANY_CAR
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY
USING (CAR_ID)
# WHERE CAR_TYPE = '세단' AND DATE_FORMAT(START_DATE, '%m') = '10'
WHERE CAR_TYPE = '세단' AND MONTH(START_DATE) = 10
ORDER BY CAR_ID DESC;
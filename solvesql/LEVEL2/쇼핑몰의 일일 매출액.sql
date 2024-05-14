SELECT
  DATE(order_purchase_timestamp) AS dt,
  ROUND(SUM(payment_value), 2) AS revenue_daily
FROM
  olist_orders_dataset
  JOIN olist_order_payments_dataset USING (order_id)
WHERE 
  dt >= '2018-01-01'
GROUP BY
  dt
ORDER BY 
  dt ASC

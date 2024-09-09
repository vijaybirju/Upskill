SELECT u.city, COUNT(t.order_id) AS total_orders
FROM users u 
LEFT OUTER JOIN trades t
ON u.user_id = t.user_id
WHERE t.status = 'Completed'
GROUP BY u.city 
ORDER BY total_orders DESC
LIMIT 3

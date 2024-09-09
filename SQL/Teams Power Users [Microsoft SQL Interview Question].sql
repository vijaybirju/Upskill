SELECT sender_id, COUNT(message_id) AS count_messages
FROM messages
WHERE EXTRACT(YEAR FROM sent_date) = 2022
AND EXTRACT(MONTH FROM sent_date) = 8
GROUP BY sender_id
ORDER BY count_messages DESC
LIMIT 2;

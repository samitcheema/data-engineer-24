SELECT 
    oi.locationId,
    MONTH(t.datetime) AS Month,
    SUM(CAST(JSON_VALUE(t.details, '$.items[0].amount') AS DECIMAL(10,2))) AS RefundAmount
FROM 
    orderItems oi 
JOIN 
    transactions t
ON oi.id = JSON_VALUE(t.details, '$.items[0].id')
WHERE 
	t.type = 'refund'
GROUP BY 
    oi.locationId, 
    MONTH(t.datetime);



select 1;

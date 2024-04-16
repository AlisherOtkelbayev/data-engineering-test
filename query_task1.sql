SELECT 
    p.transaction_date,
    SUM(
        CASE
            WHEN p.currency = 111 THEN p.amount
            ELSE p.amount * cr.exchange_rate_to_eur
        END
    ) AS 'sum(amount_eur)'
FROM 
    payments p
INNER JOIN 
    currencies c ON p.currency = c.currency_id
LEFT JOIN 
    currency_rates cr ON p.currency = cr.currency_id AND cr.exchange_date = p.transaction_date
LEFT JOIN 
    blacklist b ON p.user_id_sender = b.user_id
WHERE 
    b.user_id IS NULL
    AND c.end_date IS NULL
GROUP BY 
    p.transaction_date
ORDER BY 
    p.transaction_date;

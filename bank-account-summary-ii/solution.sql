# Write your MySQL query statement below
SELECT users.name, SUM(transactions.amount) AS balance
FROM users
JOIN transactions ON users.account = transactions.account
GROUP BY users.name
HAVING SUM(transactions.amount) > 10000;
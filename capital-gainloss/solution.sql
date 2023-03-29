# Write your MySQL query statement below

SELECT stock_name,SUM(price*((operation="SELL")* 2-1)) as capital_gain_loss from Stocks
GROUP BY stock_name

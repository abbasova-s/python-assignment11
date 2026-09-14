# Task 2: A Line Plot with Pandas

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load the DataFrame
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price 
FROM orders o 
JOIN line_items l 
ON o.order_id = l.order_id
JOIN products p 
ON l.product_id = p.product_id
 
GROUP BY o.order_id;
"""
df = pd.read_sql_query(sql_statement, conn)

# Calculate cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

# Create line plot
df.plot(x="order_id", y="cumulative", kind="line", title="Cumulative revenue vs order_id")

plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.show()


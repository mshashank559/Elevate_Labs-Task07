import sqlite3
import pandas as pd
import plotly.express as px

#Connect to DB
conn = sqlite3.connect("sales_data.db")

#Query total quantity and revenue
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)
conn.close()

#Print summary
print("Sales Summary:\n")
print(df)

#Create interactive chart
fig = px.bar(
    df,
    x="product",
    y="revenue",
    text="revenue",
    title="Revenue by Product",
    labels={"revenue": "Revenue", "product": "Product"},
    color="product"
)

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(
    xaxis_title="Product",
    yaxis_title="Revenue",
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    template="plotly_white"
)

#Save as PNG
fig.write_image("sales_chart.png", width=800, height=600)

print("Chart saved as sales_chart.png")

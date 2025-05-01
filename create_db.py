import sqlite3

# Connect and create DB
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Sample data
sales_data = [
    ("Apples", 10, 1.5),
    ("Bananas", 20, 0.5),
    ("Oranges", 15, 1.0),
    ("Apples", 5, 1.5),
    ("Bananas", 10, 0.5),
    ("Oranges", 10, 1.0)
]

# Insert data
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)

conn.commit()
conn.close()
print("Database created and populated.")

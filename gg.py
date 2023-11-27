import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('db.sqlite3')  # Replace with your database file path
cursor = conn.cursor()

# Execute a query (replace 'your_table' with the actual table name)
query = 'SELECT * FROM scrapy_app_goldprice'
cursor.execute(query)

# Fetch the data
data = cursor.fetchall()

# Get column names
column_names = [description[0] for description in cursor.description]

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=column_names)

# Save DataFrame to Excel file (replace 'output.xlsx' with your desired Excel file name)
df.to_excel('output.xlsx', index=False, engine='openpyxl')

# Close the database connection
conn.close()

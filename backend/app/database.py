import os
import sqlite3

# Connect to the database and also create it in specified  path
conn = sqlite3.connect('C:\\aaa_programovai_kodovani\\python_a_databaze\\backend\\databases\\mydatabase.db')

# Create a cursor
c = conn.cursor()

# Drop the table if it exists
c.execute("DROP TABLE IF EXISTS stocks")

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Select all rows from the 'stocks' table
c.execute('SELECT * FROM stocks')

# Fetch all rows from the last executed statement
rows = c.fetchall()

# Print all rows
for row in rows:
    print(row)

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
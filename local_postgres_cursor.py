# Template to connect to postgres on localhost

import psycopg2

# Connect to Postgres database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

# Create table
cur = conn.cursor()
cur.execute("""
    CREATE TABLE example_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INTEGER,
        email VARCHAR(255)
    );
""")
conn.commit()

# Insert data into table
cur.execute("""
    INSERT INTO example_table (name, age, email) 
    VALUES 
        ('John Smith', 30, 'john.smith@example.com'),
        ('Jane Doe', 25, 'jane.doe@example.com'),
        ('Bob Johnson', 40, 'bob.johnson@example.com');
""")
conn.commit()

# Query table
cur.execute("SELECT * FROM example_table;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close database connection
cur.close()
conn.close()

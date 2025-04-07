import mysql.connector

# Connect to MySQL Server
connection = mysql.connector.connect(
    host="localhost",          # or your server IP
    user="root",               # your MySQL username
    password="SaadSaad77300@", # your MySQL password
    database="db1"             # optional: name of the DB you want to use
)

# Check if connection is successful
if connection.is_connected():
    print("✅ Successfully connected to MySQL!")

cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")
print("✅ Table created successfully!")
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Saad", 23))
connection.commit()
print("✅ Data inserted!")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()



# query to get all tables present in database 

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")

print("Tables in the database:")
for table in cursor:
    print(table[0])

cursor.close()
conn.close()

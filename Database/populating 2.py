import mysql.connector

try:
    # Connect to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="20Eve,lyne#76",
        database="mysql"  # Connect to the default 'mysql' database
    )
    print("Connected successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

mycursor = mydb.cursor()

# Show all databases
mycursor.execute("SHOW DATABASES")
print("Databases:")
for db in mycursor:
    print(db[0])

# Switch to the 'login' database (if it exists)
try:
    mycursor.execute("USE login")
    print("Using database 'login'")
except mysql.connector.Error as err:
    print(f"Error switching to database 'login': {err}")
    mycursor.close()
    mydb.close()
    exit()

# Create a new table 'Evelyne'
try:
    mycursor.execute("""
        CREATE TABLE Rosa (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(200),
            Age INT,
            Course VARCHAR(400)
        )
    """)
    print("Table 'Rosa' created successfully")
except mysql.connector.Error as err:
    print(f"Error creating table: {err}")

# Show all tables in the current database
mycursor.execute("SHOW TABLES")
print("Tables in 'login' database:")
for table in mycursor:
    print(table[0])

# Close the cursor and connection
mycursor.close()
mydb.close()
import mysql.connector

try:
  mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "20Eve,lyne#76",
    database = "mysql"

      )
  print("Connection successful!")

except mysql.connector.Error as a:
  print(f"Error: {a}")

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
print("\t\t\tDATABASES: \n")
"""
Printing of all the databases 
"""
for db in mycursor:
  print(db)


print("")

"""
The command is used to choose the database to be used
"""
mycursor.execute("USE LOGIN")
""""
The command is used to show tables in the chosen database
"""
mycursor.execute("SHOW TABLES")
for tb in mycursor:
  print(tb)
"""
Creating another table in the login database
"""
mycursor.execute("CREATE TABLE Leaders(id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(200), Role VARCHAR(400))")
mycursor.execute("SHOW TABLES")
for ta in mycursor:
  print(ta)

"""
Deleting duplicate tables
"""
#mycursor.execute("DROP TABLE leaders")
#mycursor.execute("DROP TABLE students")
# mycursor.execute("SHOW TABLES")
# for li in mycursor:
#   print(li) 
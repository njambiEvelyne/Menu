import mysql.connector
try:
  mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "20Eve,lyne#76",
    database = "mysql"
  )
  print("Connected successfully!")

except mysql.connector.Error as err:
  print (f"Eroor: {err}")
  exit()

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Evelyne")



mycursor.execute("USE LOGIN")
#mycursor.execute("CREATE TABLE Students (ID INTEGER AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), Age INTEGER)")
mycursor.execute("SHOW TABLES")

for tb in mycursor:
  print(tb)





mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#   print(db)


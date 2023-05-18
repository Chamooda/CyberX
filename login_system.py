import mysql.connector
name = "security" # Enter table name here

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tiger",
  database="xycams"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM "+str(name))

myresult = mycursor.fetchall()
password="Pass693"

for x in myresult:
  if password == x[2]:
  	print("Success")
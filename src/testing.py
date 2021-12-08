import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Kobebryant24",
    database = "NBA"
)

mycursor = db.cursor()

mycursor.execute("select * from Divisions")

for i in mycursor:
    print(i)


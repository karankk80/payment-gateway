import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="karan", database="ecommerce"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from transactions")
for rec in mycursor:
    print(rec)
mydb.close()

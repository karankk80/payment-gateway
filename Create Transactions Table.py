# DB Connector library
import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="karan", database="ecommerce"
)

# Define a Cursor
mycursor = mydb.cursor()

# Drop a table
sql = "DROP TABLE IF EXISTS transactions"
mycursor.execute(sql)


# Create table sql
sql = """CREATE TABLE transactions (
      payment_id       VARCHAR(255) NOT NULL,
      type             VARCHAR(255),
	  amount           DECIMAL (6,2) NOT NULL,
	  currency         VARCHAR(10),
	  status           VARCHAR(255),
	  method           VARCHAR(255),
	  order_id         VARCHAR(255),
	  description      VARCHAR(255),
	  refund_status    VARCHAR(255),
	  amount_refunded  DECIMAL(6,2) NOT NULL,
	  email            VARCHAR(255),
	  contact          VARCHAR(255),
	  error_code       VARCHAR(255),
	  date_created     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (payment_id)
	  
      )"""

mycursor.execute(sql)
mycursor.execute("show tables")
# mycursor.execute("describe transactions")

for tables in mycursor:
    print(tables)


# Close the connection
mydb.close()

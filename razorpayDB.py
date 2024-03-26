# DB Connector library
import mysql.connector


# Function to insert the record in transactions table
def insert_rec(**payment_details):

    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="karan", database="ecommerce"
    )

    # Define a Cursor
    mycursor = mydb.cursor()

    sql = """ INSERT INTO transactions
               (payment_id,
                type,
                amount,
                currency,
                status,
                method,
                order_id,
                description,
                refund_status,
                amount_refunded,
                email,
                contact,
                error_code,
                date_created
                ) 
               VALUES (%s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s
                       )"""
    values = (
        payment_details["id"],
        payment_details["entity"],
        payment_details["amount"],
        payment_details["currency"],
        payment_details["status"],
        payment_details["method"],
        payment_details["order_id"],
        payment_details["description"],
        payment_details["refund_status"],
        payment_details["amount_refunded"],
        payment_details["email"],
        payment_details["contact"],
        payment_details["error_code"],
        payment_details["created_at"],
    )

    try:
        mycursor.execute(sql, values)

    except Exception as error:
        mydb.rollback()
        mydb.close()
        return error
    else:
        mydb.commit()
        mydb.close()
        return 0

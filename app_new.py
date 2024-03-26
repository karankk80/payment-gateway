import razorpay
import pgkeys
from flask import Flask, render_template, request
from random import randint
import razorpayDB
from datetime import datetime
import mysql.connector

app = Flask(__name__)

# Create a razorpay client
client = razorpay.Client(auth=(pgkeys.r_id, pgkeys.r_key))


# Function to create the 'ecommerce' database if it doesn't exist
def create_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="karan")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce")
    mydb.close()


# Call the function to create the database
create_database()


# Home page to accept the transaction information
@app.route("/")
def home_page():
    return render_template("home.html")


# Create the order before payment acceptance
def create_order(amt, descr):
    order_currency = "USD"

    # create receipt id from random number
    order_receipt = "receipt_" + str(randint(1, 1000))

    notes = {"description": descr}

    data = {
        "amount": amt,
        "currency": order_currency,
        "receipt": order_receipt,
        "notes": notes,
    }

    response = client.order.create(data)
    order_id = response["id"]
    return order_id


# Create the checkout/payment collection functionality in checkout.html
@app.route("/submit", methods=["POST"])
def app_submit():
    amt_d = request.form["amt"]
    amt = int(float(amt_d) * 100)
    descr = request.form["orderDescr"]
    fname = request.form["fname"]
    lname = request.form["lname"]
    cust_name = fname + " " + lname

    c_name = "MyFirstCompany"

    # Create an order for the transaction before payment
    order_id = create_order(amt, descr)

    return render_template(
        "checkout.html",
        custName=cust_name,
        descr=descr,
        amtD=amt_d,
        amt=amt,
        key=pgkeys.r_id,
        currency="USD",
        name=c_name,
        orderId=order_id,
    )


# Return the status of the payment
@app.route("/status", methods=["POST"])
def app_status():
    payment_id = request.form["razorpay_payment_id"]
    payment_details = client.payment.fetch(payment_id)

    payment_details["amount"] = float(payment_details["amount"]) / 100
    payment_details["amount_refunded"] = float(payment_details["amount_refunded"]) / 100
    payment_details["created_at"] = datetime.fromtimestamp(
        payment_details["created_at"]
    )

    db_status = razorpayDB.insert_rec(**payment_details)

    if db_status == 0:
        return "Payment details saved."
    else:
        return db_status


# Run the webapp
if __name__ == "__main__":
    app.run()

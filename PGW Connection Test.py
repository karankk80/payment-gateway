import razorpay
import pgkeys


# Create a razorpay client
client = razorpay.Client(auth=(pgkeys.r_id, pgkeys.r_key))

# Data dictionary
data = {"amount": 12345, "currency": "USD"}

# Create an order
response = client.order.create(data)

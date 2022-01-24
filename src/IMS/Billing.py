import json
import random
import string
from datetime import *
import smtplib
from email.message import EmailMessage
from validators import email


def Billing():

    # converting data from json format to dictionary data structure
    file1 = open("record.json", "r")
    d = file1.read()
    file1.close()
    data = json.loads(d)

    # having look at the current state of the items in the inventory
    print(" ")
    print(
        "-----------------------------------------------------Inventory of Shopkart-24/7------------------------------------------------"
    )
    print("\n")
    print(data)
    print("\n")
    print(
        "--------------------------------------------------------------------------------------------------------------------------------"
    )

    # entering the customer details and purchases made by the customer
    customer_name = input("Customer name: ")
    customer_phone = int(input("Phone number: "))
    customer_email = input("Customer Email: ")
    k = 1
    t = int(input("Number of different items purchased "))
    p = 0
    q = 0
    while t > 0:
        t = t - k
        prod_id = input("UID of item: ")
        quantity = int(input("Quantity: "))
        print(f"Product:", data[prod_id]["name"])
        print("total amount for this item: ₹", data[prod_id]["pr"] * float(quantity))
        p = p + data[prod_id]["pr"] * float(quantity)
        q = q + quantity
        print("\n")
        data[prod_id]["qn"] = data[prod_id]["qn"] - quantity
        if data[prod_id]["qn"] <= 4:
            print(
                "Warning:",
                data[prod_id]["name"],
                "will soon be out of stock, Make it available asap!",  # notifying admin whether that item will soon be out of stock.
            )
        else:
            pass

        # saving changes in the inventory after the purchase
        conv_json = json.dumps(data)
        file2 = open("record.json", "w")
        file2.write(conv_json)
        file2.close()

    # generating customer UID along with date and time
    dtime = datetime.now()
    cus_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))

    # generating bill for customer
    Bill = (
        "**********************************"
        + "\n"
        + "Bill for: "
        + customer_name
        + "\n"
        + "Phone number: "
        + str(customer_phone)
        + "\n"
        + "Customer ID: "
        + str(cus_id)
        + "\n"
        + "Bill generated on: "
        + str(dtime)
        + "\n"
        + "Quantity of items: "
        + str(q)
        + "\n"
        + "Total ₹"
        + str(p)
        + "\n"
        + "**********************************"
    )

    # storing customer data in order to keep a record of sales.
    dct = {
        "Name": customer_name,
        "Phone no": customer_phone,
        "Date": str(dtime),
        "Quantity of items": q,
        "Amount paid": p,
        "Transaction ID": str(cus_id),
    }
    temp = json.dumps(dct)
    f3 = open("sales.json", "a")
    f3.write(temp)
    f3.close()

    # mailing bill to the customer
    email = EmailMessage()
    # Who is the email from
    email["from"] = "senders_mailid"
    # To which email the bill is to be sent
    email["to"] = customer_email
    # Subject of the email
    email["subject"] = "Bill from Shopkart-24/7"
    email.set_content(
        f"Dear {customer_name}, Thanks for shopping with us!. This mail is regarding your bill. Have a nice day :)"
        + "\n"
        + "\n "
        + Bill
    )

    # Create smtp server
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        # Connect securely to server
        smtp.starttls()
        # Logging in using username and password
        smtp.login("senders_mailid", "senders_pass")
        # Send email.
        smtp.send_message(email)


Billing()

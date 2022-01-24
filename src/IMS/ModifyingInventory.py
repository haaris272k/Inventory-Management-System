import json
import getpass
import hashlib


def modify(cred1, cred2, id, password):

    # comparing hashes of the respective credentials in order to grant secure access.
    for_id = hashlib.md5(id.encode())
    for_pass = hashlib.md5(password.encode())
    if for_id.hexdigest() == cred1 and for_pass.hexdigest() == cred2:
        print("                      LOGIN SUCCESSFULL!                        ")
        # access granted
        k = 1
        print("\n")

        # adding,creating,updating or modifying the existing or new items to inventory.
        np = int(input("Number of changes to be made: "))
        while np > 0:
            np = np - k
            f = open("record.json", "r")
            r = f.read()
            f.close()
            data = json.loads(r)
            print(" ")
            print(
                "-------------------------------------------Current status of the inventory of Shopkart-24/7----------------------------------------------"
            )
            print("\n")
            print(data)
            print("\n")
            print(
                "------------------------------------------------------------------------------------------------------------------------------------------"
            )

            product_id = input("Enter product id: ")
            name_of_product = str(input("Enter name: "))
            product = int(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            data[product_id] = {"name": name_of_product, "pr": product, "qn": quantity}
            conv_js = json.dumps(data)
            f = open("record.json", "w")
            f.write(conv_js)
            f.close()
            print("\n")

        # deleting any item from the inventory.
        choice = input("Is there any item which you want to remove? ")
        if choice == "yes" or choice == "YES":
            id = input("Provide UID of the item which is to be removed ")
            del data[f"{id}"]
            print(data)
            conv_js = json.dumps(data)
            f = open("record.json", "w")
            f.write(conv_js)
            f.close()
        else:
            pass
        print("All changes were saved successully !")
    else:
        print("Access Denied!")
        exit()


cred1 = "9da8ed16798a7a29fc744b452ca6877a"
cred2 = "71288df1067d6105b4bc8abd11cac4e2"
print("-----------------LOGIN TO ACCESS THE INVENTORY-----------------")
id = str(getpass.getpass(prompt="user id "))
password = str(getpass.getpass(prompt="password "))
print("---------------------------------------------------------------")
modify(cred1, cred2, id, password)

#Grocery System v1
#import module
import json
from datetime import date #(Only imports date function)

#Try to open file if not found, creates new file
try:
    with open("grocery_data.json","r") as file:
        grocery_list = json.load(file)
except FileNotFoundError:
    grocery_list = []

#Grocery Categories
categories = ["Staple","Protein","Produce","Snacks","Drinks","Household"]

#Grocery Stores
stores = ["PicknPay","Checkers","Spar","Shoprite","Other"]

#Main Loop
while True:
    #Display CLI menu
    print(f"-----GROCERY DATA TRACKER-----\n1. Add Item\n2. View Items\n3.Total Spend\n4.Exit Tracker")

    #Error Handling
    while True:
        user_choice = input("Enter Number: ")
        try:
            user_choice = int(user_choice)
            break
        except ValueError:
            print("Invalid Entry, Enter a Number!")

    #Match Case
    match user_choice:
        case 1:
            #Add item
            #Error Handling
            while True:
                name_input = input("Enter item Name: ")
                try:
                    if name_input.strip() == "":
                        print("Invalid Entry, Please enter a valid item name!")
                        continue
                    item_name = name_input.strip()
                    break
                except ValueError:
                    print("Invalid Entry, Please enter valid item name!")
            
            while True:
                price_input = input("Enter item Price: ")
                try:
                    item_price = float(price_input)
                    break
                except ValueError:
                    print("Invalid Entry, Please enter valid item price!")

            while True:
                quantity_input = input("Enter item Quantity: ")
                try:
                    item_quantity = int(quantity_input)
                    if item_quantity <= 0:
                        print("Invalid quantity, cannot be less than 1!")
                        continue
                    break
                except ValueError:
                    print("Invalid Entry, Please enter valid item quantity!")

            print("Categories: \n")
            for i in range(len(categories)): 
                print(f"{i+1}.{categories[i]}")
            
            while True:
                category_input = input("Select item Category: ")
                try:
                    category_input = int(category_input)
                    if category_input > 0 and category_input <= len(categories):
                        category_input = category_input - 1
                        item_category = categories[category_input]
                        break
                    print("Invalid selection, please select from category list!")
                except ValueError:
                    print("Invalid Entry, please select category num!")

            print("Stores: \n")
            for i in range(len(stores)):
                print(f"{i+1}.{stores[i]}")

            while True:
                store_input = input("Select item Store: ")
                try:
                    store_input = int(store_input)
                    if  store_input < len(stores) and store_input > 0:
                        store_input = store_input - 1
                        item_store = stores[store_input]
                        break
                    print("Invalid selection, please select from store list!")
                except ValueError:
                    print("Invalid Entry, please select store num!")

            grocery_item = {"Item Name":item_name,"Price":item_price,"Quantity":item_quantity,"Date":date.today().isoformat(),"Category":item_category,"Store":item_store}
            grocery_list.append(grocery_item)
            print("Item succesfully added!")

            with open("grocery_data.json","w") as file:
                json.dump(grocery_list, file, indent = 4)
            print("Data successfully saved to Memory!")

        case 2:
            print("View Items")
        case 3:
            print("Total Spend")
        case 4:
            print("Exiting Tracker!")
            break
        case _:
            print("Wrong Value entered")


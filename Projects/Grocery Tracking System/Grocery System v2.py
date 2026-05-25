#Grocery System v2.5
#import modules
import json
import pandas as pd
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

#Functions
def get_non_empty_str(text):
    while True:
         stripped_text = input(text).strip()
         if stripped_text == "":
             print("Text cannot be empty!")
             continue
         return stripped_text.title()

#min and max boundaries are inclusive
def get_valid_num(text,number_type,min_val,max_val):
        final_num = None
        while True:
            #input
            num = input(text).strip()
            try:
                #conversion
                if number_type == int:
                    final_num = int(num)
                elif number_type == float:
                    final_num = float(num)
            except ValueError:
                print("Invalid Entry, Enter a Num!")
                continue
            #validation
            if final_num <= max_val and final_num >= min_val:
                    return final_num
            else:
                    print("Value does not meet criteria! Enter a value that meets criteria: ")
                    continue

def view_items(data_list):
    if len(data_list) == 0:
         print("There is no data to display (data is empty)")
         return
    grocery_dataframe = pd.DataFrame(data_list)
    print(grocery_dataframe)

#Main Loop
while True:
    #Display CLI menu
    print(f"----- GROCERY DATA TRACKER -----\n1. Add Item\n2. View Items\n3. View Analytics\n4. View Insights\n5. Exit Tracker")

    #User Choice
    user_choice = get_valid_num("Enter Number: ",int,1,5)

    #Match Case
    match user_choice:
        case 1:#Add item (With Function Reused in recognised patterns)
            #item Name
            item_name = get_non_empty_str("Enter item name: ")
            #item Price
            item_price = get_valid_num("Enter item Price: ",float,1.00,1000.00)
            #item Quantity
            item_quantity = get_valid_num("Enter item Quantity: ",int,1,100)

            #item Category
            print("Categories: \n")
            for i in range(len(categories)): 
                print(f"{i+1}.{categories[i]}")
        
            category_input = get_valid_num("Select item Category: ",int,1,len(categories))
            category_input -= 1
            item_category = categories[category_input]

            #item Store
            print("Stores: \n")
            for i in range(len(stores)):
                print(f"{i+1}.{stores[i]}")

            store_input = get_valid_num("Select item Store: ",int,1,len(stores))
            store_input -= 1
            item_store = stores[store_input]

            #Append and add item
            grocery_item = {"Item Name":item_name,"Price":item_price,
                            "Quantity":item_quantity,"Date":date.today().isoformat(),
                            "Category":item_category,"Store":item_store}
            
            grocery_list.append(grocery_item)
            print("Item succesfully added!")
            #Save item data   
            with open("grocery_data.json","w") as file:
                json.dump(grocery_list, file, indent = 4)
            print("Data successfully saved to Memory!")

        case 2:
            view_items(grocery_list)
        case 3:
            #View Analytics Menu
            print("------ View Analytics -----\n1. Total Spend\n2. Spend By Category\n3. Spend By Store")
            #User choice
            user_choice2 = get_valid_num("Enter number: ",int,1,3)

            match user_choice2:
                case 1: 
                    total_spend = 0 #(Initialize)
                    for item in grocery_list:
                        total_spend = total_spend + item["Price"] * item["Quantity"]
                    print(f"Overall: R{total_spend:,.2f}")
                    
                case 2: 
                    category_totals = {} #(Initialize)
                    for category in categories:
                        category_totals[category] = 0

                    for item in grocery_list:
                        item_spend = item["Price"] * item["Quantity"]
                        category_totals[item["Category"]] += item_spend

                    for category, category_spend in category_totals.items():
                        print(f"{category}, R {category_spend:,.2f}")

                case 3:
                    print("Spend by Store")
                case _:
                      print("Wrong Value entered")
            
        case 4:
            print("View Insights")
        case 5:
            print("Exiting Tracker!")
            break
        case _:
            print("Wrong Value entered")
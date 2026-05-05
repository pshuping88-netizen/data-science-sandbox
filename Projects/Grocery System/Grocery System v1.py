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

#Main Loop
while True:
    #Display CLI menu
    print(f"-----GROCERY DATA TRACKER-----\n1. Add Item\n2. View Items\n3.Total Spend\n4.Exit Tracker")
    user_choice = int(input("Enter Number: "))

    match user_choice:
        case 1:
            #Add item loop
            while True:
                loop_choice = int(input("Enter 0 to Continue / 1 to Exit: "))
                if loop_choice != 0:
                    break

                grocery_item = {"Item Name":input("Enter item Name: "),"Price":float(input("Enter item Price: ")),"Quantity":int(input("Enter item Quantity: ")),"Date":date.today().isoformat(),"Category":input("Enter item Category: "),"Store":input("Enter store Name: ")}
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


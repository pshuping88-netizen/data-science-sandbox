#GroceryLens V1.5
#import modules
import json
import pandas as pd
from datetime import date
import datetime 
import calendar

#Load/Create Grocery Data
try:
    with open("grocery_data.json","r") as file:
        grocery_list = json.load(file)
except FileNotFoundError:
    grocery_list = []

#Load/Create Budget Data
try:
    with open("grocery_budget.json", "r") as file:
        budget_data = json.load(file)
except FileNotFoundError:
    budget_data = {"monthly_budget": None}

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
                    print("Value does not meet criteria! Enter a value that meets criteria!")
                    continue

def view_items(data_list):
    if len(data_list) == 0:
         print("There is no data to display (data is empty)")
         return
    grocery_dataframe = pd.DataFrame(data_list)
    print(grocery_dataframe)

def generate_report(df):
    df = df.copy()
    #Convert Dates
    df["Date"] = pd.to_datetime(df["Date"])

    #Calculate Each record's spend (Total amount)
    df["Spend"] = df["Price"] * df["Quantity"]

    #Date Filters
    today = pd.Timestamp.today()
    month_name = calendar.month_name[today.month]
    year = today.year

    #Current Month
    current_month_df = df[(
    df["Date"].dt.year == today.year) & 
    (df["Date"].dt.month == today.month)]

    #Last Month
    if today.month == 1:
        last_month = 12
        last_year = today.year - 1
    else:
        last_month = today.month - 1
        last_year = today.year

    last_month_df = df[(
    df["Date"].dt.year == last_year) &
    (df["Date"].dt.month == last_month)]

    #Current Week
    current_week = today.isocalendar().week
    current_year = today.isocalendar().year

    current_week_df = df[(
    df["Date"].dt.isocalendar().week == current_week)&
    (df["Date"].dt.isocalendar().year == current_year)]
            
    #Last Week 
    last_week_date = today - pd.Timedelta(days=7)

    last_week = last_week_date.isocalendar().week
    last_week_year = last_week_date.isocalendar().year

    last_week_df = df[(
    df["Date"].dt.isocalendar().week == last_week)&
    (df["Date"].dt.isocalendar().year == last_week_year)]

    #CORE METRICS
    total_spend = df["Spend"].sum()

    current_month_spend = current_month_df["Spend"].sum()
    last_month_spend = last_month_df["Spend"].sum()
    current_week_spend = current_week_df["Spend"].sum()
    last_week_spend = last_week_df["Spend"].sum()

    #Budget
    budget = get_budget()

    if budget > 0:
        budget_remaining = budget - current_month_spend
        budget_used_pcnt = (current_month_spend / budget) * 100
    else:
        budget_remaining = None
        budget_used_pcnt = None

    if budget > 0:
        if budget_used_pcnt >= 100:
            budget_status = "Over Budget"
        elif budget_used_pcnt >= 80:
            budget_status = "High Usage"
        elif budget_used_pcnt >= 50:
            budget_status = "Moderate Usage"
        else:
            budget_status = "Low Usage"
    else:
        budget_status = "NO BUDGET"

    #Monthly % Change
    if last_month_spend > 0:
        month_change_pcnt = ((current_month_spend - last_month_spend) / last_month_spend) * 100
    else:
        month_change_pcnt = 0

    #Context is Current Month / Monthly
    #Top Category / Store & Spend
    category_spend = current_month_df.groupby("Category")["Spend"].sum()
    store_spend = current_month_df.groupby("Store")["Spend"].sum()

    top_category = category_spend.idxmax() if not category_spend.empty else None
    top_store = store_spend.idxmax() if not store_spend.empty else None
    
    #Spend Concentration 
    top_category_share = 0
    top_store_share = 0

    if current_month_spend > 0 and not category_spend.empty:
        top_category_share = (category_spend.max() / current_month_spend) * 100

    if current_month_spend > 0 and not store_spend.empty:
        top_store_share = (store_spend.max() / current_month_spend) * 100

    #Month Velocity (For Spend)
    month_spend_difference = current_month_spend - last_month_spend

    if last_month_spend > 0:
        month_velocity_pcnt = (month_spend_difference / last_month_spend) * 100
    else:
        month_velocity_pcnt = 0

    #Text Insight (simple rules)
    if month_velocity_pcnt > 15:
        month_velocity_insight = "Spending is accelerating strongly"
    elif month_velocity_pcnt > 5:
        month_velocity_insight = "Spending is increasing moderately"
    elif month_velocity_pcnt < -10:
        month_velocity_insight = "Spending is declining"
    else:
        month_velocity_insight = "Spending is stable"

    #Final Report
    return {
        #Core Month Report
        "current_month_spend": current_month_spend,
        "last_month_spend": last_month_spend,
        "month_change_pcnt": month_change_pcnt,
        "month_velocity_pcnt": month_velocity_pcnt,
        "month_velocity_insight": month_velocity_insight,

        #Week Context
        "current_week_spend": current_week_spend,
        "last_week_spend": last_week_spend,

        #Current Month Category / Store breakdown
        "category_spend": category_spend.to_dict(),
        "store_spend": store_spend.to_dict(),

        #Month & Year
        "month_name": month_name,
        "year": year,

        #Budget
        "budget": budget,
        "budget_remaining": budget_remaining,
        "budget_used_pcnt": budget_used_pcnt,
        "budget_status": budget_status,

        #Lifetime Context
        "total_spend": total_spend,

        #Highlights
        "top_category": top_category,
        "top_store": top_store,
        "top_category_share": top_category_share,
        "top_store_share": top_store_share
 }

def display_report(report):
    print("\n" + "="*40)
    print(f"GROCERY ANALYTICS REPORT — {report['month_name']} {report['year']}")
    print("-"*40)

    print("\nSPENDING OVERVIEW")
    print(f"Lifetime Spend:     R{report['total_spend']:,.2f}")
    print(f"This Month:         R{report['current_month_spend']:,.2f}")
    print(f"Last Month:         R{report['last_month_spend']:,.2f}")
    print(f"Trend:              {report['month_velocity_insight']} ({report['month_velocity_pcnt']:.1f}%)")

    print("\nBUDGET OVERVIEW")
    if report["budget"] > 0:
        print(f"Monthly Budget: R{report['budget']:,.2f}")
        print(f"Spent:          R{report['current_month_spend']:,.2f}")
        print(f"Remaining:      R{report['budget_remaining']:,.2f}")
        print(f"Status:         {report['budget_status']}")

        #Usage % clamping
        usage = min(max(report["budget_used_pcnt"], 0), 100)
        print(f"Usage:          {usage:.1f}%")

    else:
        print("Monthly Budget:      Not set")

    print("\nWEEKLY VIEW")
    print(f"This Week:      R{report['current_week_spend']:,.2f}")
    print(f"Last Week:      R{report['last_week_spend']:,.2f}")

    print("\nCATEGORY - SPEND BREAKDOWN (This Month)")
    for category, spend in report["category_spend"].items():
        print(f"-> {category:<10} R{spend:,.2f}")

    print("\nSTORE - SPEND BREAKDOWN (This Month)")
    for store, spend in report["store_spend"].items():
        print(f"-> {store:<10} R{spend:,.2f}")

    print("\nKEY DRIVERS & CONCENTRATION")
    print(f"Top Category:       {report['top_category']} ({report['top_category_share']:.1f}%)")
    print(f"Top Store:          {report['top_store']} ({report['top_store_share']:.1f}%)")

    print("="*40 + "\n")

def set_monthly_budget():
    global budget_data

    budget = get_valid_num("Enter monthly budget: R", float, 1, 100000)

    budget_data["monthly_budget"] = budget

    with open("grocery_budget.json", "w") as file:
        json.dump(budget_data, file, indent=4)

    print(f"Budget set to R{budget:,.2f}")

def get_budget():
    if budget_data["monthly_budget"] is None:
        return 0
    return budget_data["monthly_budget"]

#Main Loop
while True:
    #Display CLI menu
    print(f"----- GROCERY DATA TRACKER -----\n1. Add Item\n2. View Items\n3. Grocery Analytics\n4. Set Budget\n5. Exit Tracker")

    #User Choice
    user_choice = get_valid_num("Enter Number: ",int,1,5)

    #Match Case
    match user_choice:
        case 1: #Add item (With Function Reused in recognised patterns)
            #item Name
            item_name = get_non_empty_str("Enter item name: ")
            #item Price
            item_price = get_valid_num("Enter item Price: ",float,1.00,1000.00)
            #item Quantity
            item_quantity = get_valid_num("Enter item Quantity: ",int,1,100)

            #item Category
            print("Categories:\n")
            for i in range(len(categories)): 
                print(f"{i+1}.{categories[i]}")
        
            category_input = get_valid_num("Select item Category: ",int,1,len(categories))
            category_input -= 1
            item_category = categories[category_input]

            #item Store
            print("Stores:\n")
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

        case 2: #View items
            view_items(grocery_list)

        case 3: #Current State Report
            grocery_data_df = pd.DataFrame(grocery_list)
            report = generate_report(grocery_data_df)
            display_report(report)

        case 4:
            set_monthly_budget()

        case 5:
            print("Exiting Tracker!")
            break

        case _:
            print("Wrong Value entered")
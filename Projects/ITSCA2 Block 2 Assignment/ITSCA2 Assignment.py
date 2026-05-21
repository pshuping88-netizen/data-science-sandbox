#Import Modules
import pandas as pd
import matplotlib.pyplot as plt

#Exploratory Data Analysis (Question 1.3)

#Load Data
#Store data as dataframe from file
car_pricing_data = pd.read_csv("car_pricing_datasets.csv")

#Inspect Data
#Read and check data
print("Dataset Snippet:")
print(car_pricing_data.head())
print("\nMissing Values:")
print(car_pricing_data.isnull().sum())
print("\nDuplicate Records:")
print(car_pricing_data.duplicated().sum())

#Exploratory Data Analysis Visualization
#Graph 1 (Histogram): - Price Distribution
plt.figure(figsize=(10,6))
plt.hist(car_pricing_data["price"],bins=40)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#Summary Statistics
price_median = car_pricing_data["price"].median()
price_mean = car_pricing_data["price"].mean()
price_max = car_pricing_data["price"].max()
price_min = car_pricing_data["price"].min()

print(f"Price Median: R{price_median:,.2f}\nPrice Mean: R{price_mean:,.2f}\nPrice Max: R{price_max:,.2f}\nPrice Min: R{price_min:,.2f}")

#Graph 2 (Scatter plot): - Price vs Horsepower
plt.figure(figsize=(10,6))
plt.scatter(car_pricing_data["price"],car_pricing_data["horsepower"])
plt.title("Price vs Horsepower")
plt.xlabel("Price")
plt.ylabel("Horsepower")
plt.grid(True)
plt.show()

#Graph 3 (Scatter plot): - Price vs Engine Size
plt.figure(figsize=(10,6))
plt.scatter(car_pricing_data["price"],car_pricing_data["enginesize"])
plt.title("Price vs Engine Size")
plt.xlabel("Price")
plt.ylabel("Engine Size")
plt.grid(True)
plt.show()

#Graph 4(Scatter plot): - Price vs Curb Weight
plt.figure(figsize=(10,6))
plt.scatter(car_pricing_data["price"],car_pricing_data["curbweight"])
plt.title("Price vs Curb Weight")
plt.xlabel("Price")
plt.ylabel("Curb Weight")
plt.grid(True)
plt.show()

#Graph 5 (Bar Graph): - Category Relationship
avg_price_cylindernumber_data = car_pricing_data.groupby("cylindernumber")["price"].mean()#Group and store data in Series

plt.figure(figsize=(10,6))
plt.bar(avg_price_cylindernumber_data.index, avg_price_cylindernumber_data.values)
plt.title("Average Price by Cylinder Number")
plt.xlabel("Cylinder Number")
plt.ylabel("Average Price")
plt.grid(axis="y")
plt.show()

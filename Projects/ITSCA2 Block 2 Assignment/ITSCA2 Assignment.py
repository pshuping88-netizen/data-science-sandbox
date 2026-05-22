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

#Data Cleaning and Market Structure
#Filling Numerical Columns with Median
car_pricing_data["price"] = car_pricing_data["price"].fillna(price_median)

wheelbase_median = car_pricing_data["wheelbase"].median()
car_pricing_data["wheelbase"] = car_pricing_data["wheelbase"].fillna(wheelbase_median)

carlength_median = car_pricing_data["carlength"].median()
car_pricing_data["carlength"] = car_pricing_data["carlength"].fillna(carlength_median)

carwidth_median = car_pricing_data["carwidth"].median()
car_pricing_data["carwidth"] = car_pricing_data["carwidth"].fillna(carwidth_median)

carheight_median = car_pricing_data["carheight"].median()
car_pricing_data["carheight"] = car_pricing_data["carheight"].fillna(carheight_median)

curbweight_median = car_pricing_data["curbweight"].median()
car_pricing_data["curbweight"] = car_pricing_data["curbweight"].fillna(curbweight_median)

enginesize_median = car_pricing_data["enginesize"].median()
car_pricing_data["enginesize"] = car_pricing_data["enginesize"].fillna(enginesize_median)

boreratio_median = car_pricing_data["boreratio"].median()
car_pricing_data["boreratio"] = car_pricing_data["boreratio"].fillna(boreratio_median)

stroke_median = car_pricing_data["stroke"].median()
car_pricing_data["stroke"] = car_pricing_data["stroke"].fillna(stroke_median)

compressionratio_median = car_pricing_data["compressionratio"].median()
car_pricing_data["compressionratio"] = car_pricing_data["compressionratio"].fillna(compressionratio_median)

horsepower_median = car_pricing_data["horsepower"].median()
car_pricing_data["horsepower"] = car_pricing_data["horsepower"].fillna(horsepower_median)

peakrpm_median = car_pricing_data["peakrpm"].median()
car_pricing_data["peakrpm"] = car_pricing_data["peakrpm"].fillna(peakrpm_median)

citympg_median = car_pricing_data["citympg"].median()
car_pricing_data["citympg"] = car_pricing_data["citympg"].fillna(citympg_median)

highwaympg_median = car_pricing_data["highwaympg"].median()
car_pricing_data["highwaympg"] = car_pricing_data["highwaympg"].fillna(highwaympg_median)

categorical_cols = [
    "fueltype", "aspiration", "doornumber", "carbody",
    "drivewheel", "enginelocation", "enginetype",
    "cylindernumber", "fuelsystem", "CarName"
]

for column in categorical_cols:
    car_pricing_data[column] = car_pricing_data[column].fillna(
        car_pricing_data[column].mode()[0]
    )

print(car_pricing_data.isnull().sum())

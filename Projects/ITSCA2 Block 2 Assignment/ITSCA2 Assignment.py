#Import Modules
import pandas as pd


#Store data
car_pricing_data = pd.read_csv("car_pricing_datasets.csv")

#Read data
car_pricing_data.head()
car_pricing_data.info()
car_pricing_data.isnull().sum()
car_pricing_data.duplicated()
car_pricing_data.describe()
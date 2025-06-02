import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('products.csv')

# Basic statistics
print("Descriptive Statistics:")
print(df.describe())

# Group by brand and compute average price
brand_avg_price = df.groupby('Brand')['Price'].mean()
print("\nAverage Price per Brand:")
print(brand_avg_price.sort_values(ascending=False))

# Group by category and compute average stock
category_avg_stock = df.groupby('Category')['Stock'].mean()
print("\nAverage Stock per Category:")
print(category_avg_stock.sort_values(ascending=False))

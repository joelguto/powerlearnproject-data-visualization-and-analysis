import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('products.csv')

# Optional: seaborn styling
sns.set(style="whitegrid")


# 2. Bar chart: average stock per category
category_avg_stock = df.groupby('Category')['Stock'].mean().sort_values()
plt.figure(figsize=(10, 5))
category_avg_stock.plot(kind='bar')
plt.title('Average Stock per Category')
plt.xlabel('Category')
plt.ylabel('Average Stock')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Histogram: price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter plot: price vs stock
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Price', y='Stock', hue='Category', alpha=0.7)
plt.title('Price vs. Stock by Category')
plt.xlabel('Price')
plt.ylabel('Stock')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

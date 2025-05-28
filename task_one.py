import pandas as pd
try:
    df = pd.read_csv('products.csv')
    print("File loaded successfully")
    print(df.head())
except FileNotFoundError:
    print("File not found")
except pd.errors.EmptyDataError:
    print("File is empty")
except pd.errors.ParserError:
    print("File is not in the correct format")
except Exception as e:
    print("An error occurred:", e)





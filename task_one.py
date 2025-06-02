import pandas as pd
#Try to read the dataset sample in csv format
try:
    df = pd.read_csv('products.csv')
    print("File loaded successfully")
    print(df.head())
#Catch a file not found error from the read request
except FileNotFoundError:
    print("File not found")
#Catch an empty file/ data missing error on the read request
except pd.errors.EmptyDataError:
    print("File is empty")
#Catch an incorrect file format error
except pd.errors.ParserError:
    print("File is not in the correct format")
#Catch an extra exception error on the read request
except Exception as e:
    print("An error occurred:", e)





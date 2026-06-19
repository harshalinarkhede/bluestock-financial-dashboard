import pandas as pd

df = pd.read_csv(r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\companies.csv")

print("Before Cleaning:")
print(df.head())

df = df.drop_duplicates()

print("\nNull Values:")
print(df.isnull().sum())

df.to_csv(r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\companies_cleaned.csv", index=False)

print("Cleaning completed successfully!")
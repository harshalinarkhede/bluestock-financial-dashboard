import pandas as pd
from sqlalchemy import create_engine

file_path = r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\analysis.csv"

df = pd.read_csv(file_path, header=None)

# first row as header
df.columns = df.iloc[0]
df = df[1:]

# rename columns properly
df.columns = [
    "company_id",
    "period",
    "sales_growth",
    "profit_growth",
    "stock_cagr",
    "roe"
]

# remove duplicates
df = df.drop_duplicates()

print(df.head())
print(df.isnull().sum())

# save final csv
df.to_csv(
r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\analysis_final.csv",
index=False
)

# MySQL connection
engine = create_engine(
"mysql+pymysql://root:Harshu%401234@localhost/nifty_db"
)

# load into MySQL
df.to_sql(
"analysis",
con=engine,
if_exists="replace",
index=False
)

print("Analysis table loaded successfully!")
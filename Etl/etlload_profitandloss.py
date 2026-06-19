import pandas as pd
from sqlalchemy import create_engine

file_path = r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\profitandloss.csv"

df = pd.read_csv(file_path, header=None)

# first row header
df.columns = df.iloc[0]
df = df[1:]

# proper column names
df.columns = [
    "id",
    "company_id",
    "year",
    "sales",
    "expenses",
    "operating_profit",
    "opm_percentage",
    "other_income",
    "interest",
    "depreciation",
    "profit_before_tax",
    "tax_percentage",
    "net_profit",
    "eps",
    "dividend_payout"
]

df = df.drop_duplicates()

print(df.head())
print(df.isnull().sum())

df.to_csv(
r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\profitandloss_final.csv",
index=False
)

engine = create_engine(
"mysql+pymysql://root:Harshu%401234@localhost/nifty_db"
)

df.to_sql(
"profitandloss",
con=engine,
if_exists="replace",
index=False
)

print("Profit and Loss loaded successfully!")
import pandas as pd
from sqlalchemy import create_engine

# Read CSV
file_path = r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\balancesheet.csv"

df = pd.read_csv(file_path, header=None)

# First row as actual headers
df.columns = df.iloc[0]
df = df[1:]

# Rename columns properly
df.columns = [
    "id",
    "company_id",
    "year",
    "equity_share_capital",
    "reserves",
    "borrowings",
    "other_liabilities",
    "total_liabilities",
    "fixed_assets",
    "cwip",
    "investments",
    "other_assets",
    "total_assets"
]

# Remove duplicates
df = df.drop_duplicates()

print(df.head())
print(df.isnull().sum())

# Save final cleaned file
df.to_csv(
r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\balancesheet_final.csv",
index=False
)

# MySQL connection
engine = create_engine(
"mysql+pymysql://root:Harshu%401234@localhost/nifty_db"
)

# Load to MySQL
df.to_sql(
"balancesheet",
con=engine,
if_exists="replace",
index=False
)

print("Balancesheet loaded successfully!")
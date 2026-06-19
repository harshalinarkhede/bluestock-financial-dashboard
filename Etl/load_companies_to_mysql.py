import pandas as pd
from sqlalchemy import create_engine

# Read companies csv
file_path = r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\companies.csv"

df = pd.read_csv(file_path, header=None)

# First row as header
df.columns = df.iloc[0]
df = df[1:]

# Clean column names
df.columns = [
    "symbol",
    "company_logo",
    "company_name",
    "about_company",
    "website",
    "nse_profile",
    "bse_profile",
    "face_value",
    "book_value",
    "roce_percentage",
    "roe_percentage",
    "extra_col"
]

# Remove extra column
df = df.drop(columns=["extra_col"], errors="ignore")

# Remove duplicates
df = df.drop_duplicates()

# Save final cleaned csv
df.to_csv(
    r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\companies_final.csv",
    index=False
)

print("Final clean CSV created successfully!")

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:Harshu%401234@localhost/nifty_db"
)

# Load into MySQL
df.to_sql(
    "companies",
    con=engine,
    if_exists="replace",
    index=False
)

print("Companies data loaded into MySQL successfully!")
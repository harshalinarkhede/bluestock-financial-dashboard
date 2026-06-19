import pandas as pd
from sqlalchemy import create_engine

file_path = r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\prosandcons.csv"

df = pd.read_csv(file_path, header=None)

df.columns = df.iloc[0]
df = df[1:]

print(df.head())
print(df.isnull().sum())

df = df.drop_duplicates()

df.to_csv(
r"C:\Users\Manjunath Sawant\OneDrive\Desktop\Nifty Project\data\clean\prosandcons_final.csv",
index=False
)

engine = create_engine(
"mysql+pymysql://root:Harshu%401234@localhost/nifty_db"
)

df.to_sql(
"prosandcons",
con=engine,
if_exists="replace",
index=False
)

print("Pros and Cons loaded successfully!")
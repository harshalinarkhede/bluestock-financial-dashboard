import pandas as pd
import os

raw_path = "data/raw"
clean_path = "data/clean"

os.makedirs(clean_path, exist_ok=True)

files = [
    "companies.xlsx",
    "analysis.xlsx",
    "balancesheet.xlsx",
    "profitandloss.xlsx",
    "cashflow.xlsx",
    "prosandcons.xlsx",
    "documents.xlsx"
]

for file in files:
    file_path = os.path.join(raw_path, file)

    df = pd.read_excel(file_path)

    csv_name = file.replace(".xlsx", ".csv")
    output_path = os.path.join(clean_path, csv_name)

    df.to_csv(output_path, index=False)

    print(f"{file} converted successfully")

print("All files converted successfully!")
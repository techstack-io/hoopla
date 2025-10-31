import pandas as pd

# 1️⃣ Load your Excel file
path = r"C:\Users\dan\Downloads\visits.xlsx"
df = pd.read_excel(path)
print(f"Loaded {len(df):,} rows with columns: {list(df.columns)}")

# 2️⃣ Filter to only product-related pages
product_df = df[df["Page URL"].str.contains(r"product|products|sku|item", case=False, na=False)]
print(f"Filtered to {len(product_df):,} product-page visits.")

# 3️⃣ Drop rows without company info
product_df = product_df[product_df["Company Name"].notna()]

# 4️⃣ Keep only the key columns
matched = product_df[["Company Name", "Page URL", "Page Title", "Visit start date"]]

# 5️⃣ Save the matched table
output_path = r"C:\Users\dan\Downloads\company_page_visits.csv"
matched.to_csv(output_path, index=False)
print(f"✅ Saved matched company–page data to {output_path}")

# 6️⃣ (Optional) preview top results
print(matched.head(10))

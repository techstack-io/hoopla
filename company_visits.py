import pandas as pd

# 1. Load your Excel file
df = pd.read_excel(r"C:\Users\dan\Downloads\visits.xlsx")

# 2. Filter for product pages (you can adjust the keywords)
product_df = df[df["Page URL"].str.contains(r"product|products|sku|item", case=False, na=False)]

# 3. Drop rows without a company name
product_df = product_df[product_df["Company Name"].notna()]

# 4. Count visits by company
company_visits = (
    product_df.groupby("Company Name")
    .size()
    .reset_index(name="product_page_visits")
    .sort_values("product_page_visits", ascending=False)
)

# 5. Save results
company_visits.to_csv(r"C:\Users\dan\Downloads\company_product_visits.csv", index=False)

print("✅ Saved company visit summary to C:\\Users\\dan\\Downloads\\company_product_visits.csv")

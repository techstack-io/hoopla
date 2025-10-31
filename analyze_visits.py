from clean_data import load_data, filter_product_pages, summarize_by_company

path = r"C:\Users\dan\Downloads\visits.xlsx"

df = load_data(path)

# match your Excel column names exactly
product_df = filter_product_pages(df, url_col="Page URL")

summary_df = summarize_by_company(
    product_df,
    company_col="Company Name",
    url_col="Page URL",
    time_col="Visit start date"
)

summary_df.to_csv(r"C:\Users\dan\Downloads\product_page_summary.csv", index=True)

print("✅ Saved summarized product page data to C:\\Users\\dan\\Downloads\\product_page_summary.csv")

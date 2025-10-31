"""
clean_data.py
-------------
Purpose: extract, clean, and summarize product-page visits by company
from a raw visitor log (Excel or CSV). Keeps heavy lifting local to
avoid overloading APIs.
"""

import pandas as pd
import re
from typing import Optional

PRODUCT_PATTERN = re.compile(r"/(product|products|sku|item)/", re.IGNORECASE)


def load_data(path: str) -> pd.DataFrame:
    """Load Excel or CSV automatically based on file extension."""
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)
    return df


def filter_product_pages(df: pd.DataFrame, url_col: str = "url") -> pd.DataFrame:
    """Keep only rows where the URL likely refers to a product page."""
    if url_col not in df.columns:
        raise ValueError(f"Column '{url_col}' not found in dataset.")
    return df[df[url_col].str.contains(PRODUCT_PATTERN, na=False)]


def summarize_by_company(
    df: pd.DataFrame,
    company_col: str = "company",
    url_col: str = "url",
    time_col: Optional[str] = None,
) -> pd.DataFrame:
    """Aggregate visits, unique pages, and optionally time range by company."""
    if company_col not in df.columns:
        raise ValueError(f"Column '{company_col}' not found in dataset.")

    agg_dict = {
        url_col: ["count", pd.Series.nunique],
    }
    if time_col and time_col in df.columns:
        agg_dict[time_col] = ["min", "max"]

    summary = df.groupby(company_col).agg(agg_dict)
    summary.columns = ["visits", "unique_pages", "first_visit", "last_visit"][
        : len(summary.columns)
    ]
    summary = summary.sort_values("visits", ascending=False)
    summary["high_intent"] = summary["visits"] > 5
    return summary


def clean_and_summarize(path: str) -> pd.DataFrame:
    """Load, clean, and return a summary of product-page visits."""
    df = load_data(path)
    print(f"Loaded {len(df):,} rows with {len(df.columns)} columns.")

    product_df = filter_product_pages(df)
    print(f"Filtered to {len(product_df):,} product-page visits.")

    summary = summarize_by_company(product_df)
    print(f"Generated summary for {len(summary):,} companies.")
    return summary


if __name__ == "__main__":
    # Example usage
    file_path = "visits.xlsx"  # change to your actual file path
    summary_df = clean_and_summarize(file_path)
    print(summary_df.head(20))

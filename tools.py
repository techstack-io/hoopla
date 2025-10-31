import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Global DataFrame reference
_current_df = None

def set_dataframe(df: pd.DataFrame):
    """Set the current DataFrame for analysis"""
    global _current_df
    _current_df = df

def get_dataframe() -> pd.DataFrame:
    """Get the current DataFrame"""
    return _current_df

def summarize_df() -> str:
    """Summarize the current DataFrame with basic statistics."""
    df = get_dataframe()
    if df is None:
        return "No data loaded. Please upload a CSV file first."
    
    summary = f"""
    Dataset Summary:
    - Shape: {df.shape[0]} rows × {df.shape[1]} columns
    - Columns: {', '.join(df.columns)}
    
    Numeric Column Statistics:
    {df.describe().to_string()}
    
    Missing Values:
    {df.isnull().sum().to_string()}
    """
    return summary

def filter_df(column: str, value: str) -> pd.DataFrame:
    df = get_dataframe()
    if df is None:
        st.warning("No data loaded.")
        return None
    filtered = df[df[column] == value]
    st.write(f"Filtered to {len(filtered)} rows where {column} = {value}")
    return filtered


def plot_column(column: str, plot_type: str = "histogram") -> str:
    """Plot a column from the DataFrame."""
    df = get_dataframe()
    if df is None:
        return "No data loaded."
    
    fig, ax = plt.subplots()
    if column not in df.columns:
        return f"Column '{column}' not found in DataFrame."

    if plot_type == "histogram":
        df[column].hist(ax=ax)
    elif plot_type == "bar":
        df[column].value_counts().plot(kind='bar', ax=ax)
    else:
        df[column].plot(ax=ax)
    
    ax.set_title(f"{column} - {plot_type}")
    st.pyplot(fig)
    return f"Plotted {column} as {plot_type}"
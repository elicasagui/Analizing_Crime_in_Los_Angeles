# src/visualize.py

import pandas as pd
import matplotlib.pyplot as plt


def load_data(csv_path: str) -> pd.DataFrame:
    """
    Load the crimes CSV into a pandas DataFrame.
    """
    df = pd.read_csv(csv_path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the raw crime DataFrame:
    - Parse 'DATE OCC' as datetime
    - Standardize column names to lowercase
    - Drop rows with missing date or missing essential columns
    """
    df = df.copy()
    # Standardize column names
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # Parse 'date_occ' into datetime
    if 'date_occ' in df.columns:
        df['date_occ'] = pd.to_datetime(df['date_occ'], format='%Y-%m-%d', errors='coerce')
    else:
        df['date_occ'] = pd.to_datetime(df.get('date_rptd', None), format='%Y-%m-%d', errors='coerce')

    # Drop rows without valid date
    df = df.dropna(subset=['date_occ'])

    return df


def plot_time_series(
    df: pd.DataFrame,
    date_column: str = 'date_occ',
    resample_freq: str = 'M',
    title: str = "Monthly Crime Counts"
) -> plt.Figure:
    """
    Generate a time series line plot of crime counts aggregated by the given frequency.
    Returns a Matplotlib Figure.
    """
    ts = df.set_index(date_column).sort_index()
    counts = ts.resample(resample_freq).size()

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(counts.index, counts.values, marker='o', linestyle='-')
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Crimes')
    plt.tight_layout()
    return fig


def plot_top_crime_types(
    df: pd.DataFrame,
    category_col: str = 'crm_cd_desc',
    top_n: int = 10,
    title: str = "Top Crime Types"
) -> plt.Figure:
    """
    Generate a bar chart of the top N most frequent crime types.
    Returns a Matplotlib Figure.
    """
    counts = df[category_col].value_counts().nlargest(top_n)
    fig, ax = plt.subplots(figsize=(8, 4))
    counts.sort_values().plot.barh(ax=ax, color='steelblue')
    ax.set_title(title)
    ax.set_xlabel('Number of Incidents')
    ax.set_ylabel('Crime Type')
    plt.tight_layout()
    return fig

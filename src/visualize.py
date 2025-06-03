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
    - Standardize column names to lowercase and underscores
    - Parse 'DATE_OCC' as datetime
    - Drop rows with missing date
    - Ensure numeric columns are properly typed
    """
    df = df.copy()
    # Standardize column names
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # Parse 'date_occ' into datetime
    if 'date_occ' in df.columns:
        df['date_occ'] = pd.to_datetime(df['date_occ'], format='%Y-%m-%d', errors='coerce')
    else:
        df['date_occ'] = pd.to_datetime(df.get('date_rptd', None), format='%Y-%m-%d', errors='coerce')

    # Drop rows without a valid date
    df = df.dropna(subset=['date_occ'])

    # Convert numeric columns if needed
    if 'vict_age' in df.columns:
        df['vict_age'] = pd.to_numeric(df['vict_age'], errors='coerce')
    if 'time_occ' in df.columns:
        df['time_occ'] = pd.to_numeric(df['time_occ'], errors='coerce')

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


def summarize_by_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create victim age groups and count number of crimes per age group.
    Returns a DataFrame with columns ['age_group', 'count'].
    """
    bins = [0, 12, 18, 25, 40, 60, 120]
    labels = ['0-12', '13-18', '19-25', '26-40', '41-60', '61+']
    df = df.copy()
    df['age_group'] = pd.cut(df['vict_age'], bins=bins, labels=labels, right=True)
    age_summary = df.groupby('age_group').size().reset_index(name='count')
    return age_summary


def summarize_by_victim_sex(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count crimes by victim sex (M/F/U).
    Returns a DataFrame with columns ['vict_sex', 'count'].
    """
    sex_summary = df['vict_sex'].value_counts().reset_index()
    sex_summary.columns = ['vict_sex', 'count']
    return sex_summary


def summarize_by_victim_ethnicity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count crimes by victim ethnicity (vict_descent).
    Returns a DataFrame with columns ['vict_descent', 'count'].
    """
    eth_summary = df['vict_descent'].value_counts().reset_index()
    eth_summary.columns = ['vict_descent', 'count']
    return eth_summary


def summarize_by_weapon(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Count crimes by weapon description and return top_n.
    Returns a DataFrame with columns ['weapon_desc', 'count'].
    """
    weapon_summary = df['weapon_desc'].value_counts().nlargest(top_n).reset_index()
    weapon_summary.columns = ['weapon_desc', 'count']
    return weapon_summary

# src/dashboard.py

import os
import sys

# Add project root and src folder to sys.path for module resolution
current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(os.path.dirname(current_file), os.pardir))
src_path = os.path.join(project_root, "src")
for path in (project_root, src_path):
    if path not in sys.path:
        sys.path.insert(0, path)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.visualize import (
    load_data,
    clean_data,
    plot_time_series,
    plot_top_crime_types
)


@st.cache_data
def load_and_clean(csv_path: str) -> pd.DataFrame:
    """
    Load and clean data, cached to avoid reloading on every interaction.
    """
    raw_df = load_data(csv_path)
    clean_df = clean_data(raw_df)
    return clean_df


def main():
    st.set_page_config(
        page_title="LA Crime Dashboard",
        layout="wide"
    )

    st.title("Crime in Los Angeles – Interactive Dashboard")

    # Sidebar filters
    st.sidebar.header("Filters")
    df = load_and_clean("data/crimes.csv")

    # Date range filter
    min_date = df['date_occ'].min()
    max_date = df['date_occ'].max()
    date_range = st.sidebar.date_input(
        "Date range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    # Crime category filter
    if 'crm_cd_desc' in df.columns:
        crime_options = df['crm_cd_desc'].unique().tolist()
    else:
        crime_options = []
    selected_crimes = st.sidebar.multiselect(
        "Crime Types",
        options=sorted(crime_options),
        default=[]
    )

    # Neighborhood (area_name) filter
    if 'area_name' in df.columns:
        neighborhood_options = df['area_name'].unique().tolist()
    else:
        neighborhood_options = []
    selected_neighborhoods = st.sidebar.multiselect(
        "Neighborhoods",
        options=sorted(neighborhood_options),
        default=[]
    )

    st.sidebar.markdown("---")
    if st.sidebar.button("Reset Filters"):
        selected_crimes = []
        selected_neighborhoods = []
        date_range = [min_date, max_date]

    # Apply filters
    mask = (df['date_occ'] >= pd.to_datetime(date_range[0])) & \
           (df['date_occ'] <= pd.to_datetime(date_range[1]))
    filtered_df = df[mask]

    if selected_crimes:
        filtered_df = filtered_df[filtered_df['crm_cd_desc'].isin(selected_crimes)]
    if selected_neighborhoods:
        filtered_df = filtered_df[filtered_df['area_name'].isin(selected_neighborhoods)]

    # Display key metrics
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Crimes", f"{len(filtered_df):,}")
    col2.metric("Unique Crime Types", f"{filtered_df['crm_cd_desc'].nunique()}")
    col3.metric("Unique Neighborhoods", f"{filtered_df['area_name'].nunique()}")

    # Time Series Plot
    st.subheader("Crime Trend Over Time")
    fig_ts = plot_time_series(
        filtered_df,
        date_column='date_occ',
        resample_freq='M',
        title="Monthly Crime Counts"
    )
    st.pyplot(fig_ts)

    # Top Crime Types
    st.subheader("Top Crime Types")
    fig_top = plot_top_crime_types(
        filtered_df,
        category_col='crm_cd_desc',
        top_n=10,
        title="Top 10 Crime Types"
    )
    st.pyplot(fig_top)

    # Additional Metrics: Crimes by Neighborhood
    st.subheader("Crime Counts by Neighborhood")
    if 'area_name' in filtered_df.columns:
        counts_by_neighborhood = (
            filtered_df['area_name']
            .value_counts()
            .rename_axis('Neighborhood')
            .reset_index(name='Count')
        )
        st.dataframe(counts_by_neighborhood)

    # Additional Metrics: Crimes by Hour of Day
    st.subheader("Crime Counts by Hour of Day")
    if 'time_occ' in filtered_df.columns:
        df_time = filtered_df.copy()
        df_time['time_str'] = df_time['time_occ'].astype(str).str.zfill(4)
        df_time['hour'] = df_time['time_str'].str[:2].astype(int)
        counts_by_hour = df_time['hour'].value_counts().sort_index()
        fig_hour, ax_hour = plt.subplots(figsize=(8, 3))
        ax_hour.bar(counts_by_hour.index, counts_by_hour.values, color='coral')
        ax_hour.set_xlabel("Hour of Day")
        ax_hour.set_ylabel("Number of Crimes")
        ax_hour.set_title("Crime Distribution by Hour")
        st.pyplot(fig_hour)

    # Additional Metrics: Monthly Crime Distribution (as pivot table)
    st.subheader("Monthly Crime Distribution (Pivot Table)")
    df_heat = filtered_df.copy()
    df_heat['year_month'] = df_heat['date_occ'].dt.to_period("M")
    heat_data = (
        df_heat
        .groupby(['year_month', 'area_name'])
        .size()
        .unstack(fill_value=0)
    )
    st.dataframe(heat_data)


if __name__ == "__main__":
    main()

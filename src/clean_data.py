def clean_nobel_data(df):
    df = df.dropna(subset=['year', 'category', 'birth_country'])
    df['year'] = df['year'].astype(int)
    return df

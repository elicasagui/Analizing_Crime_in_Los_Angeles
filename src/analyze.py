def count_prizes_by_category(df):
    return df['category'].value_counts()

def prizes_over_time(df):
    return df.groupby('year').size()

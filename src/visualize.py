import matplotlib.pyplot as plt
import seaborn as sns

def plot_category_distribution(category_counts):
    plt.figure(figsize=(10,6))
    sns.barplot(x=category_counts.values, y=category_counts.index)
    plt.title("Nobel Prizes by Category")
    plt.xlabel("Count")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig('notebooks/images/category_distribution.png')

def plot_prizes_over_time(prizes_per_year):
    plt.figure(figsize=(12,6))
    prizes_per_year.plot(kind='line')
    plt.title("Nobel Prizes Awarded Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Prizes")
    plt.tight_layout()
    plt.savefig('notebooks/images/prizes_over_time.png')

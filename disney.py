import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import ast

# Load the dataset
df = pd.read_csv('./data_set/disney_plus_shows.csv')

# Display basic information about the dataset
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())

# Check for missing values in the genre column
print(f"\nMissing values in 'genre' column: {df['genre'].isnull().sum()}")

# Clean the data - remove rows with missing genres
df_clean = df.dropna(subset=['genre'])

print(f"Remaining shows after cleaning: {len(df_clean)}")

# Function to extract and count genres
def analyze_genre_distribution(df):
    all_genres = []
    
    for genre_string in df['genre']:
        # Split genres by comma and strip whitespace
        if pd.notna(genre_string):
            genres = [genre.strip() for genre in str(genre_string).split(',')]
            all_genres.extend(genres)
    
    # Count frequency of each genre
    genre_counts = Counter(all_genres)
    
    return genre_counts

# Get genre distribution
genre_distribution = analyze_genre_distribution(df_clean)

# Display top genres
print("\nTop 15 Most Common Genres:")
for genre, count in genre_distribution.most_common(15):
    print(f"{genre}: {count} shows")

# Create visualization
plt.figure(figsize=(12, 8))

# Get top 15 genres for the plot
top_genres = dict(genre_distribution.most_common(15))

# Create bar chart
plt.barh(list(top_genres.keys()), list(top_genres.values()))
plt.xlabel('Number of Shows')
plt.ylabel('Genre')
plt.title('Top 15 Most Common Genres on Disney+')
plt.gca().invert_yaxis()  # Show highest count at top

# Add value labels on bars
for i, (genre, count) in enumerate(top_genres.items()):
    plt.text(
        count + 1, i, str(count)
    )
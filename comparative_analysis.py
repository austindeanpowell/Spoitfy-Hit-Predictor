import pandas as pd

# Load integrated dataset
df = pd.read_csv('final_spotify_dataset')


# Verify data and column added
print(df[['duration_ms', 'duration_min']].head())

# Check basic info
print(df.head())
print(df.info())

# Convert 'billboard_rank' to numeric, setting errors to NaN
df['billboard_rank'] = pd.to_numeric(df['billboard_rank'], errors='coerce')

#recalling source of spotify high and low
high_popularity_df = df[df['source'] == 'Spotify_High']
low_popularity_df = df[df['source'] == 'Spotify_Low']

#calculating the averages of attributes 
attributes = ['speechiness', 'valence', 'tempo', 'loudness', 'duration_min', 'popularity_numeric','acousticness','liveness']

avg_high_popularity = high_popularity_df[attributes].mean()
avg_low_popularity = low_popularity_df[attributes].mean()

# Print averages clearly for comparison
print(" Average Attributes for High Popularity Tracks:")
print(avg_high_popularity.round(2))

print("\n Average Attributes for Low Popularity Tracks:")
print(avg_low_popularity.round(2))
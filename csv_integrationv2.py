import pandas as pd

# Load dataset to inspect columns
df = pd.read_csv('spotify_combined_dataset.csv')

print(df.columns.tolist())
df.rename(columns={
    'track_name': 'Track_Name',
    'track_artist': 'Artist',
    'track_popularity': 'Popularity',
    'playlist_genre': 'Genre',
    'playlist_name': 'Playlist_Name',
    'duration_ms': 'Duration_ms',
    'energy': 'Energy',
    'danceability': 'Danceability',
    'tempo': 'Tempo',
    'valence': 'Valence',
    'speechiness': 'Speechiness',
    'loudness': 'Loudness',
    'acousticness': 'Acousticness',
    'instrumentalness':'Instrumentalness',
    'source':'Source',
}, inplace=True)

# Fill missing categorical values
categorical_cols = ['Genre', 'Playlist_Name', 'Artist']
for col in categorical_cols:
    df[col] = df[col].fillna('Unknown')

# Save cleaned and filled dataset
df.to_csv('spotify_final_clean.csv', index=False)

print("✨ Final merged and cleaned dataset saved as 'spotify_final_clean.csv'")
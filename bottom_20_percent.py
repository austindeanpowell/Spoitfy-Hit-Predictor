import pandas as pd
import os

# Load data
df = pd.read_csv('low_popularity_spotify_data.csv')

# Define bottom 20% tracks
df['popularity_category'] = pd.qcut(df['track_popularity'], q=[0, 0.8, 1], labels=['LOW POPULARITY', 'LOWEST POPULARITY'])

# Filter specifically for lowest popularity tracks
lowest_tracks = df[df['popularity_category'] == 'LOWEST POPULARITY']

# Define your target folder (change this to your desired path)
output_folder = '/Users/austinpowell/Desktop/Music Dataset/spotify_analysis'

# Make sure the folder exists (creates it if not present)
os.makedirs(output_folder, exist_ok=True)

# Define the output file path (clearly naming lowest popularity)
output_path = os.path.join(output_folder, 'bottom_20_percent_lowest_tracks.csv')

# Save the file
lowest_tracks.to_csv(output_path, index=False)

print(f"✅ Lowest popularity tracks saved to: {output_path}")

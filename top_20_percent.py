import pandas as pd
import os

# Load data
df = pd.read_csv('high_popularity_spotify_data.csv')

# Define top 20% tracks
df['popularity_category'] = pd.qcut(df['track_popularity'], q=[0, 0.8, 1], labels=['POPULAR', 'HIGH POPULARITY'])

# Filter for top tracks only
top_tracks = df[df['popularity_category'] == 'HIGH POPULARITY']

# Define your target folder (change this to your desired path)
output_folder = '/Users/austinpowell/Desktop/Music Dataset'

# Make sure the folder exists (optional - if you're 100% sure it's there, you can skip this line)
os.makedirs(output_folder, exist_ok=True)

# Define the output file path
output_path = os.path.join(output_folder, 'top_20_percent_tracks.csv')

# Save the file
top_tracks.to_csv(output_path, index=False)

print(f"✅ Top tracks saved to: {output_path}")

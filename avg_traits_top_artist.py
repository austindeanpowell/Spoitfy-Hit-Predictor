import pandas as pd
import os

# Load data
df = pd.read_csv('top_20_percent_tracks.csv')


average_traits = df [[ 
    'valence','danceability','energy','speechiness','tempo','track_popularity'
]].mean().reset_index()

# Rename columns for clarity
average_traits.columns = ['Trait', 'Average Value']


# Define your target folder (change this to your desired path)
output_folder = '/Users/austinpowell/Desktop/Music Dataset'

# Make sure the folder exists (optional - if you're 100% sure it's there, you can skip this line)
os.makedirs(output_folder, exist_ok=True)

# Define the output file path
output_path = os.path.join(output_folder, 'average_song_traits.csv')

# Save the file
average_traits.to_csv(output_path, index=False)

print(f"\n✅ average_song_traits.csv {output_path}\n")
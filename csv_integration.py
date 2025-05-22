import pandas as pd
import os

# Load datasets
top_20_df = pd.read_csv('top_20_percent_tracks.csv')
bottom_20_df = pd.read_csv('bottom_20_percent_lowest_tracks.csv')

# Add 'source' identification to track dataset origin
top_20_df['source'] = 'Spotify_Top20_Percentile'
bottom_20_df['source'] = 'Spotify_Bottom20_Percentile'

# Combine datasets into one unified DataFrame
spotify_combined = pd.concat(
    [top_20_df, bottom_20_df],
    ignore_index=True
)

# Quick verification
print("✨ Combined Spotify Data Preview:")
print(spotify_combined.head())

# Save to a new CSV for further analysis
spotify_combined.to_csv('spotify_combined_dataset.csv', index=False)

print("\n🎉 Spotify integration complete! Saved as 'spotify_combined_dataset.csv'")
# Export final dataset for analysis


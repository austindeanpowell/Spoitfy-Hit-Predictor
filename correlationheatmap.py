import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import os

# Load data
df = pd.read_csv('high_popularity_spotify_data.csv')

#top_tracks = df[df[ 'popularity_category']== 'HIGH POPULARITY']

#Define feautures to compare

traits=['energy', 'tempo', 'danceability','valence','speechiness']

#calculate Correlation Matrix
corr = df[traits +['track_popularity']].corr()

plt.figure(figsize=(8,5))
sns.heatmap(corr, annot= True, cmap='coolwarm', fmt='.2f')
plt.title('Trait Correlation To High Popularity Songs')
plt.show()
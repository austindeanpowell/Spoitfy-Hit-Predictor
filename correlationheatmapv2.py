import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import os

# Load data
df = pd.read_csv('high_popularity_spotify_data.csv')

#top_tracks = df[df[ 'popularity_category']== 'HIGH POPULARITY']

#Define feautures to compare

traits=['liveness','loudness','key','duration_ms','acousticness','instrumentalness']
#calculate Correlation Matrix
corr = df[traits +['track_popularity']].corr()

plt.figure(figsize=(8,5))
sns.heatmap(corr, annot= True, cmap='coolwarm', fmt='.2f')
plt.title('Trait Correlation In High Popularity Songs')
plt.show()
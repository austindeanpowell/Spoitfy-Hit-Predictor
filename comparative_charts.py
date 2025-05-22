import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 

df = pd.read_csv('finalspotify_dataset.csv')



#recalling source of spotify high and low
high_popularity_df = df[df['popularity_Catergory'] == 'High_POPULARITY']
low_popularity_df = df[df['popularity_Catergory'] == 'Low_Popularity']

# Attributes list
attributes = ['energy','danceability','instrumentalness','key','speechiness', 'valence', 'tempo', 'loudness', 'duration_min','track_popularity','acousticness','liveness']

# Add popularity_numeric to distinguish categories
high_popularity_df['popularity_numeric'] = 1
low_popularity_df['popularity_numeric'] = 0

# Combine the datasets
combined_df = pd.concat([high_popularity_df, low_popularity_df], ignore_index=True)

# Attributes to compare
attributes = ['speechiness', 'valence', 'tempo', 'loudness', 'duration_min']
num_attributes = len(attributes)

# Calculate the averages grouped by popularity
avg_values = combined_df.groupby('popularity_numeric')[attributes].mean()
high_values = avg_values.loc[1].tolist()
low_values = avg_values.loc[0].tolist()

# Radar chart setup
angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()

# Complete the loop for radar chart
high_values += high_values[:1]
low_values += low_values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
ax.fill(angles, high_values, color='green', alpha=0.3, label='High Popularity')
ax.fill(angles, low_values, color='red', alpha=0.3, label='Low Popularity')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes)

# Calculate averages again for clarity
avg_high_popularity = high_popularity_df[attributes].mean()
avg_low_popularity = low_popularity_df[attributes].mean()

# Combine both averages into a single DataFrame for easy plotting
avg_df = pd.DataFrame({
    'High Popularity': avg_high_popularity,
    'Low Popularity': avg_low_popularity
}).reset_index().rename(columns={'index': 'Attribute'})




# Melt the DataFrame for better visualization
avg_df_melted = avg_df.melt(id_vars='Attribute', var_name='Popularity', value_name='Average Value')

# Set visual style
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))

# Plotting
sns.barplot(data=avg_df_melted, x='Attribute', y='Average Value', hue='Popularity', palette='viridis')

# Customize the plot
plt.title('🎶 Average Musical Attributes: High vs Low Popularity Tracks', fontsize=16, fontweight='bold')
plt.xlabel('Musical Attribute', fontsize=14)
plt.ylabel('Average Value', fontsize=14)
plt.legend(title='Track Popularity', fontsize=12, title_fontsize=13)

# Display plot
plt.tight_layout()
plt.show()

#violin plot
attributes = ['speechiness', 'valence', 'tempo']
for attribute in attributes:
    plt.figure(figsize=(10, 5))
    sns.violinplot(data=[high_popularity_df[attribute], low_popularity_df[attribute]], palette='muted')
    plt.xticks([0, 1], ['High Popularity', 'Low Popularity'])
    plt.title(f'Distribution of {attribute.capitalize()}')
    plt.xlabel('Popularity Category')
    plt.ylabel(attribute.capitalize())
    plt.show()

# Combine datasets and create popularity numeric indicator
high_popularity_df['popularity_numeric'] = 1
low_popularity_df['popularity_numeric'] = 0
combined_df = pd.concat([high_popularity_df, low_popularity_df])

# Correlation calculation
corr_matrix = combined_df[['speechiness', 'valence', 'tempo', 'loudness', 'duration_min', 'popularity_numeric','acousticness','liveness']].corr()

# Heatmap visualization
plt.figure(figsize=(10, 7))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap with Track Popularity')
plt.show()

attributes = ['speechiness', 'valence', 'tempo','acousticness','liveness']
for attribute in attributes:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=[high_popularity_df[attribute], low_popularity_df[attribute]], palette='Set2')
    plt.xticks([0, 1], ['High Popularity', 'Low Popularity'])
    plt.title(f'Boxplot of {attribute.capitalize()}')
    plt.xlabel('Popularity Category')
    plt.ylabel(attribute.capitalize())
    plt.show()

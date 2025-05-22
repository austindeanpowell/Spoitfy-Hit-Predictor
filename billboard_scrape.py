import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Billboard URL for 2024 Top 100
url = "https://www.billboard.com/charts/year-end/hot-100-songs/"

# Set User-Agent to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Updated selectors for Billboard (2024)
songs = soup.find_all('div', class_='o-chart-results-list-row-container')

# Empty lists for data
rankings, titles, artists = [], [], []

# Extract data carefully with error handling
for song in songs:
    rank_tag = song.find('span', class_='c-label')
    title_tag = song.find('h3', class_='c-title')
    artist_tag = song.select_one('span.c-label.a-font-primary-s')
    artist = artist_tag.text.strip() if artist_tag else 'N/A'

    if rank_tag and title_tag and artist_tag:
        rankings.append(rank_tag.text.strip())
        titles.append(title_tag.text.strip())
        artists.append(artist_tag.text.strip())
    else:
        print(f"⚠️ Missing data for a song. Skipped entry.")

# Create DataFrame
df = pd.DataFrame({
    'Rank': rankings,
    'Title': titles,
    'Artist': artists
})

# Define your target folder (change this to your desired path)
output_folder = '/Users/austinpowell/Desktop/Music Dataset/spotify_analysis'

# Make sure the folder exists (creates it if not present)
os.makedirs(output_folder, exist_ok=True)

# Define the output file path (clearly naming lowest popularity)
output_path = os.path.join(output_folder, 'billboard_hot100_2024.csv')

# Save the file
df.to_csv(output_path, index=False)

print(f"✅ CSV printed to: {output_path}")

# Save CSV
df.to_csv('billboard_hot100_2024.csv', index=False)
print("🎉 CSV successfully created: billboard_hot100_2024.csv")
print(df.head(10))

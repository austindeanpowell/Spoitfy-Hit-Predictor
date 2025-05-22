import pandas as pd

# Load your dataset
df = pd.read_csv('finalspotify_dataset.csv', encoding='latin1')

# List of columns you want to convert
numeric_cols = [
    'energy', 'tempo', 'danceability', 'loudness', 'liveness',
    'valence', 'instrumentalness', 'track_popularity',
    'key', 'duration_min', 'acousticness'
]

# Strip any whitespace and convert to float
#astype(str).str.strip() → ensures values like ' 0.85 ' become '0.85'
for col in numeric_cols:
    df[col] = df[col].astype(str).str.strip()  # Clean string version
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to float

# Optional: Check for missing values caused by invalid conversions
print(df[numeric_cols].isnull().sum())
print(df.dtypes)

df.to_csv('finalspotify_dataset_cleaned.csv', index=False)

print("✅ Cleaned dataset saved as 'finalspotify_dataset_cleaned.csv'")

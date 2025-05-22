import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# Load the cleaned Spotify dataset

# Load data
df = pd.read_csv('finalspotify_dataset_cleaned.csv')
print("Loaded shape:", df.shape)

# Columns to use
features = ['energy', 'tempo', 'danceability', 'loudness', 'liveness',
            'valence', 'speechiness', 'instrumentalness', 'key',
            'duration_min', 'acousticness']

# Check if all features and target exist
required_cols = features + ['track_popularity']
missing_cols = [col for col in required_cols if col not in df.columns]
if missing_cols:
    print(f"Missing columns: {missing_cols}")
    exit()

# Convert relevant columns to numeric
df[required_cols] = df[required_cols].apply(pd.to_numeric, errors='coerce')

# Drop rows only where required columns have NaNs
df.dropna(subset=required_cols, inplace=True)
print("After cleaning shape:", df.shape)

# Set up features and target
X = df[features]
y = df['track_popularity']

print("Final X shape:", X.shape)
print("Final y shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#####################################################################

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"📈 R² Score: {r2:.2f}")
print(f"📉 Mean Squared Error: {mse:.2f}")

import joblib

joblib.dump(model, 'hit_predictor_model.pkl')  # Save the trained model

scaler = StandardScaler()
# Fit on training data, then transform training data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) 


# Save it
joblib.dump(scaler, 'scaler.pkl')

model_features = ['energy', 'tempo', 'danceability', 'loudness', 'liveness',
            'valence', 'speechiness', 'instrumentalness', 'key',
            'duration_min', 'acousticness']

import json
with open('model_features.json', 'w') as f:
    json.dump(model_features, f)
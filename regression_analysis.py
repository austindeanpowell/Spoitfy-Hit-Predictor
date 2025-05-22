import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('finalspotify_dataset_cleaned.csv')

# Convert object columns to numeric
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.dropna(inplace=True)

# Define features & target (regression)
features = ['instrumentalness','speechiness', 'valence', 'tempo', 'loudness', 'key',
            'danceability', 'energy', 'duration_min','liveness','acousticness']
target = 'track_popularity'

X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models to compare
models = {
    'LinearRegression': LinearRegression(),
    'RandomForestRegressor': RandomForestRegressor(n_estimators=100, random_state=42),
    'XGBRegressor': XGBRegressor(n_estimators=100, random_state=42),
    'SVR': SVR()
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    results[name] = {'MSE': mse, 'R2': r2}
    print(f"{name} → MSE: {mse:.2f} | R²: {r2:.2f}")

# Optional: Bar Chart for Visual Comparison
model_names = list(results.keys())
mse_scores = [results[model]['MSE'] for model in model_names]
r2_scores = [results[model]['R2'] for model in model_names]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(model_names, mse_scores, color='coral')
plt.title('Mean Squared Error (MSE)')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.bar(model_names, r2_scores, color='teal')
plt.title('R² Score')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# Load and prepare data
df = pd.read_csv('finalspotify_dataset_cleaned.csv')


# Ensure popularity_numeric is defined (1 for high popularity, 0 for low)
df['popularity_numeric'] = df['popularity_Catergory'].apply(lambda x: 1 if x in ['High_Popularity'] else 0)

# Define features and target
features = ['track_popularity','instrumentalness','speechiness', 'valence', 'tempo', 'loudness', 'key','danceability', 'energy', 'duration_min','liveness','acousticness']

X = df[features]
y = df['popularity_numeric']


# Select only numeric columns from X
X_numeric = X.select_dtypes(include=['number'])


# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(X.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# Feature importance using Random Forest
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

importances = pd.Series(rf.feature_importances_, index=features)
importances.sort_values(ascending=False).plot(kind='bar', title='Feature Importance')
plt.ylabel('Importance')
plt.xlabel('Features')
plt.show()

y_pred = rf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

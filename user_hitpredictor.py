import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import joblib
import pandas as pd
import json
df = pd.read_csv('finalspotify_dataset_cleaned.csv')
import streamlit as st

# Load trained model and scaler
model = joblib.load('hit_predictor_model.pkl')
scaler = joblib.load('scaler.pkl')
with open('model_features.json') as f:
    model_features = json.load(f)

#Access spotify API
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='684adb962c0e4aa583463fecd822d3c9',
    client_secret='17e421de520845868f338a26a9bdfb90',
    redirect_uri='http://localhost:8888/callback',
    scope='user-library-read'
))

# ----------------- APP FUNCTIONS ------------------------------ #
def get_song_features(track_id):
    try:
        features = sp.audio_features(track_id)
        if features and features[0] is not None:
            return features[0]
        else:
            st.warning(f"Track ID {track_id} returned no features. It might be private or unavailable.")
            return None
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status == 403:
            st.error(f"Access denied for track {track_id}. This might be due to region-locking or API restrictions.")
        else:
            st.error(f"Spotify error for track {track_id}: {str(e)}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred while fetching features for track {track_id}: {str(e)}")
        return None

def preprocess_features(raw):
    duration_min = raw['duration_ms'] / 60000

    features_dict = {
        'danceability': raw['danceability'],
        'energy': raw['energy'],
        'valence': raw['valence'],
        'loudness': raw['loudness'],
        'speechiness': raw['speechiness'],
        'acousticness': raw['acousticness'],
        'instrumentalness': raw['instrumentalness'],
        'liveness': raw['liveness'],
        'tempo': raw['tempo'],
        'duration_min': duration_min,
        'key': raw['key'],
        'mode': raw['mode'],

     }

    return pd.DataFrame([features_dict])[model_features]


# ------------------ Streamlit UI ------------------ #
    st.title("🎧 Hit Predictor: Audio-Based Popularity Estimator")

track = st.text_input("Enter a song name:")

if track:
    raw = get_song_features(track)
    if raw:
        processed = preprocess_features(raw)
        scaled = scaler.transform(processed)
        score = model.predict(scaled)[0]
        st.success(f"Predicted Popularity Score: {round(score, 2)} / 100")
    else:
        st.error("Could not find the track. Try another one.")
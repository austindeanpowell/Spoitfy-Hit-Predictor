import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def verify_spotify_api():
    try:
        client_credentials_manager = SpotifyClientCredentials(
            client_id='f88bd7ee4606415ab54add0bf91cdf4e',
            client_secret='a98cfce912d54190835564886b02dd5f'
        )
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Test track
        test_track_id = '11dFghVXANMlKmJXsNCbNl'  # Carly Rae Jepsen
        logging.info("🔍 Verifying Spotify API access with test track...")
        features = sp.audio_features([test_track_id])

        if features and features[0] is not None:
            logging.info("✅ Spotify API access verified successfully.")
            return sp
        else:
            logging.warning("⚠️ Received empty or null features.")
            return None

    except spotipy.exceptions.SpotifyException as e:
        logging.error(f"❌ SpotifyExceptionnnnn: {e}")
        return None

    except Exception as e:
        logging.error(f"🚨 Unexpected error: {e}")
        return None

# Run the check
if __name__ == '__main__':
    if verify_spotify_api():
        print("All good — Spotify API is accessible ✅")
    else:
        print("Something went wrong with Spotify API access ❌")

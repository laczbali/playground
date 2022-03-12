import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

load_dotenv()
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SCOPES = os.environ.get('SPOTIFY_SCOPES')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope=SCOPES))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

# results = sp.devices()
# for item in results["devices"]:
#     print(item)

# results = sp.current_user_playlists()
# for item in results["items"]:
#     print(item["name"], item["tracks"]["total"])
# print(results["items"][0])

sp.shuffle(
    device_id="ecaa8ede2790d16c9d6bf713629ecb9b8342fa06",
    state=True
)

sp.volume(
    device_id="ecaa8ede2790d16c9d6bf713629ecb9b8342fa06",
    volume_percent=50
)

sp.start_playback(
    device_id='ecaa8ede2790d16c9d6bf713629ecb9b8342fa06',
    context_uri='spotify:playlist:5Wceuwzk7euT3uqNzsYQFl',
    offset={"position": random.randint(0, 56)}
)
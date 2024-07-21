import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


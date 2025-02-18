import billboard
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Configuración de Spotify API
client_id = 'e1da22184fb64d32a8f288c3f1bf9a84'  # Reemplaza con tu Client ID de Spotify
client_secret = '78fdfc8d4fc9402aa52b816d3309dae0'  # Reemplaza con tu Client Secret de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Función para obtener las características de audio de una canción
def get_audio_features(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        audio_features = sp.audio_features(track_id)
        return audio_features[0] if audio_features else None
    return None

# Obtener las listas de Billboard Hot 100
years = [2022, 2023, 2024]
data = []

for year in years:
    chart = billboard.ChartData('hot-100', year=year)
    for song in chart:
        track_name = song.title
        artist_name = song.artist
        audio_features = get_audio_features(track_name, artist_name)
        if audio_features:
            song_data = {
                'year': year,
                'title': track_name,
                'artist': artist_name,
                'danceability': audio_features['danceability'],
                'energy': audio_features['energy'],
                'key': audio_features['key'],
                'loudness': audio_features['loudness'],
                'mode': audio_features['mode'],
                'speechiness': audio_features['speechiness'],
                'acousticness': audio_features['acousticness'],
                'instrumentalness': audio_features['instrumentalness'],
                'liveness': audio_features['liveness'],
                'valence': audio_features['valence'],
                'tempo': audio_features['tempo'],
            }
            data.append(song_data)

# Crear un DataFrame y guardar en CSV
df = pd.DataFrame(data)
df.to_csv('billboard_hot_100_audio_features.csv', index=False)
print("Dataset guardado en 'billboard_hot_100_audio_features.csv'")


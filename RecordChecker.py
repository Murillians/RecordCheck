import requests
import secrets


# Singleton class that gets spotify access token
class requestInitalizer():
    _instance = None
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               "grant_type": f'client_credentials&client_id={secrets.spotifyClientId}&client_secret={secrets.spotifyClientSecret}'}
    r = requests.get('https://accounts.spotify.com/api/token', headers=headers)
    access_token = r.json()['access_token']
    token_type = r.json()['token_type']

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getAuthTokens(self):
        return ['Authorization: Bearer ' + self.access_token]


class Album:
    artist = ""
    title = ""
    artworkURL = ""
    recordLabel = ""

    def __init__(self, artist, title, artworkURL):
        self.artist = artist
        self.title = title
        self.artworkURL = artworkURL


def getAlbum():
    tokens = requestInitalizer()
    r = requests.get("")


def spotifySearch(query):
    tokens = requestInitalizer().getAuthTokens()
    r = requests.get('https://api.spotify.com/v1/search' + f'?q={query}' + "&type=album,artist", headers=tokens)
    print(r.json())

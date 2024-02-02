import requests
import secrets
import json

# Singleton class that gets spotify access token
class requestInitalizer():
    _instance = None
    data = {
        'grant_type': 'client_credentials',
        'client_id': secrets.spotifyClientId,
        'client_secret': secrets.spotifyClientSecret,
    }
    r = requests.post('https://accounts.spotify.com/api/token', data=data)
    access_token = r.json()['access_token']
    token_type = r.json()['token_type']

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getAuthTokens(self):
        return {'Authorization': "Bearer " + self.access_token}


class Album:
    artist = ""
    artistUri = ""
    title = ""
    artworkURL = ""
    spotifyUri=""
    def __init__(self, artist,artistUri ,title, artworkURL,spotifyUri):
        self.artist = artist
        self.artistLink = artistUri
        self.title = title
        self.artworkURL = artworkURL
        self.spotifyUri = spotifyUri
    def toString(self):
        return f"Artist: {self.artist} \nArtist Link: {self.artistLink} \nTitle: {self.title} \nArtwork URL: {self.artworkURL} \nSpotify URL: {self.spotifyUri}"
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
def getAlbum():
    tokens = requestInitalizer()
    r = requests.get("")


def spotifySearch(query):
    tokens = requestInitalizer().getAuthTokens()
    params = {"q": query, "type": "album,artist"}
    r = requests.get('https://api.spotify.com/v1/search',params=params , headers=tokens)
    f=open("albums.json","w")
    f.write(r.text)
    return searchCleaner(r.json()['albums']['items'])
def searchCleaner(results):
    albums=[]
    for album in results:
        tempAlbum=Album(album['artists'][0]['name'],album['artists'][0]['uri'], album['name'], album['images'][0]['url'],album['uri'])
        albums.append(tempAlbum)
        print(tempAlbum.toJson())
    return albums


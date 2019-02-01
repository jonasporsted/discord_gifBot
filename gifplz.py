import requests

# Giphy
random_url = "https://api.giphy.com/v1/gifs/random"
api_key_value = "ljUA9SfDJ3MlGgiUGypcpIhq3oG5iB8C"

def hent_gif_url(søgeord):

    parametre = {
        "api_key": api_key_value,
        "tag": søgeord
    }

    response = requests.get(
        url=random_url,
        params=parametre,
    )

    data = response.json()
    billede = data["data"]["images"]["downsized_large"]["url"]
    return billede

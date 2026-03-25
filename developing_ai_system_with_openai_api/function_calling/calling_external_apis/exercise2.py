"""
Packaging the API Call as a Function
"""
import requests

def get_artwork(keyword):
    url = "https://api.artic.edu/api/v1/artworks/search"

    params = {
        "q": keyword
    }

    response = requests.get(url, params=params)

    return response.json()

print(get_artwork("monet"))
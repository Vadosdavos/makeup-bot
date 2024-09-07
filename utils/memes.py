import requests

async def get_memes():
    url = "https://api.imgflip.com/get_memes"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['data']['memes']
    else:
        print(f"Error: {response.status_code}")
        return []
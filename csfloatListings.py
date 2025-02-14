import requests

KEY = "plzdI0AwkenafVMG1tFFFdjxxCg7V3wr"
url = "https://csfloat.com/api/v1/listings"

def getItem():
    params ={
        "market_hash_name": "Revolver Case",
        "sort_by": "lowest_price",
        "limit": 1,
    }
    headers = {
        "Authorization": KEY
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    steamID = data['data'][0]['seller']['steam_id']
    return steamID



getItem()



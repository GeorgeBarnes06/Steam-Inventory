import requests, json
from addToJSON import addToJSON
from steam_web_api import Steam

steamKey = "30A82DDACF2D0FB7834ABD5133D34ED3"
steam = Steam(steamKey)

def fetch_inventory_data(steamID):
    inventory_url = f"https://steamcommunity.com/inventory/{steamID}/730/2?l=english&count=5000"
    response = requests.get(inventory_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch inventory.")
        return None

def parse_inventory(data):
    if not data:
        return {}
    descriptions = data.get("descriptions")
    with open("hashNames.json", "r") as file:
        data = json.load(file)
    for item in descriptions:
        marketHashName = item.get("market_hash_name")
        classID = item.get("classid")
        if "Case" in marketHashName:
            if marketHashName not in data:
                data[marketHashName] = classID
    addToJSON("hashNames.json", data)

def main():
    steamID = "76561197960275286"
    data = fetch_inventory_data(steamID)
    if data:
        parse_inventory(data)
    else:
        print("No data found.")

if __name__ == "__main__":
    main() 
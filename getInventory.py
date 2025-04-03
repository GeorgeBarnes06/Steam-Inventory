import requests, json
from steam_web_api import Steam
from getSteamKey import getSteamKey

steamKey = getSteamKey()
steam = Steam(steamKey)

def getID(link):
    try:
        linkSplit = link.split("/")
        if "id" in link:
            userID = (linkSplit[-2])
            user = steam.users.search_user(userID)
            steamID = user["player"]["steamid"]
        else:
            steamID = (linkSplit[-1])
        return steamID
    except:
        print("invalid link entered")

def loadIventory(steamID):
    inventoryLink = ("https://steamcommunity.com/inventory/" + steamID + "/730/2?l=english&count=5000")
    response = requests.get(inventoryLink)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch inventory page")

def fetchInventory(steamLink):
    steamID = getID(steamLink)
    inventory = loadIventory(steamID)
    return inventory

#https://steamcommunity.com/profiles/76561198799576372 
#https://steamcommunity.com/id/_fuz_/


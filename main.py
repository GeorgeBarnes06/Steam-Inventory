import requests, re, json
from steam_web_api import Steam
from bs4 import BeautifulSoup
from steam_web_api import Steam

steamKey = "30A82DDACF2D0FB7834ABD5133D34ED3"
steam = Steam(steamKey)

def getInventory(steamID):
    inventoryLink = ("https://steamcommunity.com/inventory/" + steamID + "/730/2?l=english&count=5000")
    response = requests.get(inventoryLink)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch inventory page")

def getSteamID(link):
    try:
        if len(link.split("/")) == 6: #detemining if custom link or not
            userID = link.split("/")[-2]
            user = steam.users.search_user(userID)
            steamID = user['player']['steamid']
            return steamID
        else: #not custom link
            steamID = link.split("/")
            return (str(steamID[-1]))[:-1]
    except:
        print("Invalid Steam Link")
        return None

def getCases(items):
    #descriptions does not contain each individual case so we use assets instead
    #have to loop through descriptions and match the class ids
    descriptions = items.get("descriptions")
    assets = items.get("assets")
    IDtoHashName = {}
    caseInventory = {}
    totalCases = 0
    with open ("hashNames.json", "r") as file:
        cases = json.load(file)
    for item in descriptions: #map each description#
        IDtoHashName[item.get("classid")] = item.get("market_hash_name")
    for item in assets:
        classID = (item["classid"])
        marketHashName = (IDtoHashName[classID])
        if "Case" in marketHashName:
            if marketHashName in caseInventory:
                caseInventory[marketHashName] += 1
            else:
                caseInventory[marketHashName] = 1
            totalCases += 1
    return (totalCases, caseInventory)


def main():
    link = "https://steamcommunity.com/id/_fuz_/"
    steamID = getSteamID(link)
    if steamID:
        inventory = getInventory(steamID)
        totalCases, cases = getCases(inventory)
        print(totalCases)
        print(cases)

#https://steamcommunity.com/profiles/76561198799576372 
#https://steamcommunity.com/id/_fuz_/

if __name__ == "__main__":
    main()


'''
1. input steam link
2. get/find steam id
3. process id and load iventory
4. check each item and check if its case
5. add to dicitonary cases
6. output 

'''
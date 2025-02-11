import requests, re, json
from steam_web_api import Steam
from bs4 import BeautifulSoup
import time
from steam_web_api import Steam

steamKey = "###"
steam = Steam(steamKey)

def getInventory(profile):
    if "/id" not in profile: #check if custom url or not
        profile += "/"
    profile +=  "inventory#730"
    response = requests.get(profile)
    if response.status_code == 200:
        return response
    else:
        print("Failed to fetch inventory page")

def countItems(inventory):
        soup = BeautifulSoup(inventory.text, "html.parser")
        CS_tag = soup.find("a", href="#730")
        if CS_tag:
            cs_items_span = CS_tag.find("span", class_="games_list_tab_number")
            item_count = (re.findall(r'\d+', (str(cs_items_span))))
            getCases(item_count[0], soup)
        else:
            print("No cs2 items found")

def getCases(itemCount, soup):
    inventory_html = soup.find("div", class_="inventory_page")

def test(id):
    user = steam.users.search_user(id)
    steamID = user['player']['steamid']
    inventoryLink = ("https://steamcommunity.com/inventory/" + steamID + "/730/2?l=english&count=5000")
    response = requests.get(inventoryLink)#
    if response.status_code == 200:
        data = response.json()
        print(data['assets'])
    else:
        print("Failed to fetch inventory page")

link = "https://steamcommunity.com/profiles/76561198799576372"
inv = getInventory(link)
countItems(inv)
test("_fuz_")

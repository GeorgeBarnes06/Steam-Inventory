from getInventory import fetchInventory
from parseInventory import parseInventory
from storeInventory import storeInventory, newTemplate

def main(link):
    inventory = (fetchInventory(link))
    cases = parseInventory(inventory)
    newTemplate()
    storeInventory(cases, link)

if __name__ == "__main__":
    main("https://steamcommunity.com/profiles/76561198799576372")

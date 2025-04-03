import json

def parseInventory(inventory):
    descriptions = inventory.get("descriptions")
    assets = inventory.get("assets")
    IDtoHashName = {}
    caseInventory = {}
    totalCases = 0
    caseNames = getCaseNames()
    for item in descriptions: #map each description#
        IDtoHashName[item.get("classid")] = item.get("market_hash_name")
    for item in assets:
        classID = (item["classid"])
        marketHashName = (IDtoHashName[classID])
        if marketHashName in caseNames:
            if marketHashName in caseInventory:
                caseInventory[marketHashName] += 1
            else:
                caseInventory[marketHashName] = 1
            totalCases += 1
    result = {
        "totalCases": totalCases,
        "cases": caseInventory
    }
    return result

def getCaseNames():
    with open("hashNames.json", "r") as file:
        cases = json.load(file)
    caseNames = list(cases.keys())
    return caseNames

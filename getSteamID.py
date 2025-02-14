from steam_web_api import Steam

steamKey = "30A82DDACF2D0FB7834ABD5133D34ED3"
steam = Steam(steamKey)

def getSteamID(link):
    user = steam.users.search_user(link)
    id = user['player']['steamid']
    return id

print(getSteamID('Shitlaren'))
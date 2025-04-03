def getSteamKey():
    with open("steamKey.txt", "r") as file:
        return file.read().strip()
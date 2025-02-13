import json

def addToJSON(fileName, data):
    with open(fileName, 'r') as file: #load current file
        currentData = json.load(file)
    if isinstance(currentData, dict):  # Ensure the data structure is a dict
        currentData.update(data)
    else:
        print("JSON file not dict")
        return None
    with open(fileName, 'w') as file:
        json.dump(currentData, file, indent=4)


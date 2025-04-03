import pandas as pd

def storeInventory(cases=None, link=None):
    new_row = [{'URL': link, 'CS items': 'y', 'Number of cases': cases['totalCases']}]
    new_df = pd.DataFrame(new_row)
    new_df.to_csv("inventories.csv", mode='a', index=False, header=False)

def newTemplate():
    file = "inventories.csv"
    headers = ['URL', 'CS items', 'Number of cases']
    df = pd.DataFrame(columns=headers)
    df.to_csv(file, index=False)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
import numpy as np
from datetime import datetime
#url = "https://api.coincap.io/v2/assets/bitcoin/"
date = datetime.now().strftime("%Y%m%d")


payload={}
headers = {}

## If we want to know a list of coins from the API, we can use this function
'''
## EXTRA: Outputs all current id's from the file
def all_current_ids():
    url = "https://api.coincap.io/v2/assets/"
    ## Request Output
    response = requests.request("GET", url, headers=headers, data=payload)
    ## Outputs based on requested field
    info = json.loads(response.text)['data']
    ## grabs the length of the object
    len(info)
    x = 0
    coin_list = []
    while x < len(info):    
        coin_list.append(info[x]['id'])
        x += 1
    return coin_list
    
print(all_current_ids()   )
'''


## Ids for different functions
assets_ids = ["bitcoin", "ethereum", 'binance-coin']
ex_ids2 = ["kraken", "mxc-com"]


## Fields for different functions
assets_fields = ["id", "symbol", "name", "rank", "priceUsd"]
exchanges_fields = ["exchangeId", "name", "rank", "exchangeUrl"]


    

## Asset information for desired coins and converts to a list
def coin_assets (coins, fields):
    ## Create your desired column names
    assets_data = [["id","symbol","name","rank","price"]]
    ## Loops to grab each Coin name
    for coin in coins:
        ## Creates empty list table to append in full table set
        add_data = []
        ## Loops to grab desired fields
        for data_info in fields:  
            ## Create URL for each Coin
            url = "https://api.coincap.io/v2/assets/" + coin
            ## Request Output
            response = requests.request("GET", url, headers=headers, data=payload)
            ## Outputs based on requested field
            info = json.loads(response.text)['data'][data_info]
            ## Add info
            add_data.append(info)
        ## Appends to full dataset
        assets_data.append(add_data)
    return assets_data    

# Exchanges information for desired coins and converts to a list
def coin_exchanges (coins, fields):
    ## Create your desired column names
    exchanges_data = [["id", "name", "rank", "Url"]]
    ## Loops to grab each Coin name
    for coin1 in coins:
        ## Creates empty list table to append in full table set
        add_data = []
        ## Loops to grab desired fields
        for data_info2 in fields:  
            ## Create URL for each Coin
            url = "https://api.coincap.io/v2/exchanges/" + coin1
            ## Request Output
            response = requests.request("GET", url, headers=headers, data=payload)
            ## Outputs based on requested field
            info = json.loads(response.text)['data'][data_info2]
            # Add info
            add_data.append(info)
        ## Appends to full dataset   
        exchanges_data.append(add_data)
    return exchanges_data


# Prints Output
coin_assets = coin_assets(assets_ids,assets_fields)
coin_exchanges = coin_exchanges(ex_ids2,exchanges_fields)

# save file
np.savetxt(f"C:\dev\csdev\coin_assets_info_{date}.csv",coin_assets, delimiter =", ", fmt ='% s')
np.savetxt(f"C:\dev\csdev\coin_exchanges_info_{date}.csv",coin_exchanges,delimiter =", ", fmt ='% s')
    
    
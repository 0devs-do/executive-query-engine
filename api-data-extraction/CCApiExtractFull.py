
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:40:06 2023

@author: Martin
"""

##  1. Keeps the original top 5 Exchanges by Volume
##  2. Takes the next 5 based Top Rank by TradingPair

import requests
import json
import numpy as np
from datetime import datetime
import config
from config import SETTINGS
import os
staging_folder = config.SETTINGS['staging_folder']

# Date Value
date = datetime.now().strftime("%Y%m%d")

payload={}
headers = {}

### Coin Market Function
def coin_markets():
    # Request market data
    url = "https://api.coincap.io/v2/markets"
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # Request the data output
    info = json.loads(response.text)["data"]
    
    # Create a List for Columns and Values
    market_data = []
    
    # Create List for Columns
    market_columns = []
    
    # Retrieve Field Names
    for column_names in info[0]:
        market_columns.append(column_names)
        
    # Append to Full List
    market_data.append(market_columns)
    
    # Retrieve all information for each grouping
    x = 0
    while x < len(info):
        market_values = []
        for columns in market_columns:
            market_values.append(info[x][columns])
        x += 1
        market_data.append(market_values) 
        
    # When Function is called, return the Full List with Column and Values   
    return market_data

### Coin Assets Function
def coin_assets():
    # Request market APIS
    url = "https://api.coincap.io/v2/assets"
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # Request the data output
    info2 = json.loads(response.text)["data"]
    
    # Create a List for Columns and Values   
    assets_data = []
    
    # Create List for Columns
    assets_columns = []
    
    # Retrieve Field Names
    for column_names in info2[0]:
        assets_columns.append(column_names)
        
    # Append to Full List    
    assets_data.append(assets_columns)
    
    # Retrieve all information for each grouping
    x1 = 0
    while x1 < len(info2):
        assets_values = []
        for columns in assets_columns:
            assets_values.append(info2[x1][columns])
        x1 += 1
        assets_data.append(assets_values) 
        
    # When Function is called, return the Full List with Column and Values           
    return assets_data

def coin_exchanges():
    # Request market APIS
    url = "https://api.coincap.io/v2/exchanges"
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # Request the data output   
    info3 = json.loads(response.text)["data"]

    # Create a List for Columns and Values 
    exchanges_data = []

    # Create List for Columns
    exchanges_columns = []
    
    # Retrieve Field Names  
    for column_names in info3[0]:
        exchanges_columns.append(column_names)
        
    # Append to Full List            
    exchanges_data.append(exchanges_columns)
    
    # Retrieve all information for each grouping
    x2 = 0
    while x2 < len(info3):
        exchanges_values = []
        for columns in exchanges_columns:
            exchanges_values.append(info3[x2][columns])
        x2 += 1
        exchanges_data.append(exchanges_values) 
    
    # When Function is called, return the Full List with Column and Values
    return exchanges_data

# Assigns output to variables
# In this case, returns lists to deisgnated variables
coin_market = coin_markets()
coin_assets = coin_assets()
coin_exchanges = coin_exchanges()
 


# Save Files
np.savetxt(staging_folder+f"\coin_markets_{date}.csv",coin_market, delimiter =", ", fmt ='% s')
#np.savetxt(f"C:\dev\csdev\coin_assets_info1_{date}.csv",coin_market, delimiter =", ", fmt ='% s')
np.savetxt(staging_folder+f"\coin_assets_{date}.csv",coin_assets, delimiter =", ", fmt ='% s')
np.savetxt(staging_folder+f"\coin_exchanges_{date}.csv",coin_exchanges,delimiter =", ", fmt ='% s')


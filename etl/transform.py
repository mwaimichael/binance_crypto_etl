from extract import get_crypto_price
import pandas as pd
from datetime import date

def transform_data():

    # get data from the extraction function
    data = get_crypto_price()


    # get the crypto/asset symbol and price
    target_assets = ['BTCUSDT', 'WBTCUSDT', 'USDTIDR', 'USDTBIDR', 'USDTIDRT', 'XAUTUSDT', 'PAXGUSDT', 'USDTCOP', 'YFIUSDT', 'WBETHUSDT']

    # get data of target assets only
    filtered_data = {
        item.get("symbol"): round(float(item.get("weightedAvgPrice")), 2) 
        for item in data 
        if item.get("symbol") in target_assets
    }
    
    # convert dictionary to dataframe
    df = pd.DataFrame(filtered_data, index=[0])
    df.index = [pd.Timestamp.today().normalize()]


    # reset index and fix date as a column
    df.reset_index(inplace=True)
    df.columns = ['date', *target_assets]
    
    return df



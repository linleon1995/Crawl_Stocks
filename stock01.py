#!/usr/bin/python
# -*- coding: utf-8 -*-

#%%
import requests
from io import StringIO
import pandas as pd
import numpy as np
import requests

import json

YAHOO = ["https://query1.finance.yahoo.com/v8/finance/chart/", "&interval=1d&events=history&=hP2rOschxO0"]

def get_stock_price(code, period):
    """
    Args:
        code: A String. Stock code.
        period: A Tuple inclucdes two numbers represents starting time and ending time.
    Returns:
        stock_price: Specific time period for stock price.
    """
    stock_code = code + "?"
    stock_time = "period1=" + str(period[0]) + "&period2=" + str(period[1])
    site = YAHOO
    site.insert(1, stock_code)
    site.insert(2, stock_time)
    
    response = requests.get("".join(site))
    response.text[:1000]

    data = json.loads(response.text)
    df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))

    return df


# %%
# TODO: change time foramt
# TODO: capture error while user input wrong stock code or stock time.
if __name__ == '__main__':
    df = get_stock_price("2882.TW", (0, 1517722857))
    df.head()
    df.close.plot()

# %%

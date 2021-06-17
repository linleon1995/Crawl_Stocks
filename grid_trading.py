#%%
from typing import Iterator
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HISTORY = "history/BTCUSDT-4h-data.csv"

def back_test_data(backtest_data):
    return pd.read_csv(backtest_data).iterrows()

class BaseGridTrading():
    # TODO: check bad setting error, too high or too low price
    # TODO: check bad setting error, grid too small or too big
    # TODO: Get assest information from Binance
    def __init__(self, assest, low, high, grid_range,
    range_mode,
                 stop_cond="out_range",
                 min_assest=None):
        """
        Args:
            assest: starting property
            low: Lowest price of grid
            high: Highest price of grid
            range: Price range of grid

        """
        self.trading_ratio = 0.05 # Total assest need to be 1/trading_ratio times of trading amount
        self.low = low
        self.high = high
        self.range = grid_range
        self.history = back_test_data(HISTORY)

        # TODO: general case for select trading coin in self.pair
        self.coin_pair = [coin for coin in assest]
        self.get_current_price()
        self.grid = tuple(range(self.low, self.high, self.range))
        print(self.grid)
        self.set_current_grid()
        self.stop_cond = stop_cond
        
        self.range_mode = range_mode
        self.first_trade = False
        self.assest = assest # {"BTC": btc_assest, "USDT": usdt_assest}
        if min_assest is not None:
            self.min_assest = min_assest
        else:
            self.min_assest = None # TODO: min = current BTC price (USDT) * BTC amount + USDT amount

    def set_current_grid(self):
        cur_price = self.price[2]
        if cur_price > self.high:
            self.cur_grid = (self.grid[-2], self.grid[-1])
        elif cur_price < self.low:
            self.cur_grid = (self.grid[0], self.grid[1])
        else:
            print(cur_price, len(self.grid), int((cur_price-self.low)/self.range+1), self.range)
            self.cur_grid = (self.grid[int((cur_price-self.low)/self.range)],
                             self.grid[int((cur_price-self.low)/self.range+1)])

    def get_current_price(self):
        idx, row = next(self.history)
        self.price = (idx, row["timestamp"], row["close"])
        # self.price = None
        # if self.trading_mode == "realworld":
        #     pass
        # elif self.trading_mode == "backtest":
        #     self.price = next(self.history)
        # else:
        #     raise ValueError("Unknown trading mode.")
    
    def trading(self):
        # TODO: check the time difference between condition match and actual trading
        # Trading command
        self.get_current_price()
        self.first_trade = True
        if self.price[2] <= self.cur_grid[0]:
            trading_type = "Buy"
        elif self.price[2] >= self.cur_grid[1]:
            trading_type = "Sell"
        amount = self.price[2] / self.min_assest

        # Trade
        print(self.price, self.cur_grid, trading_type)
        trading_info = (trading_type, amount, self.coin_pair[0])
        # TODO: Actual interact with website
        # TODO: catch trading fail error
        return trading_info

    def analysis(self, trading_info):
        self.update_grid()

    def __call__(self):
        while True:
            self.get_current_price()
            cur_price = self.price[2]
            if cur_price > self.low and cur_price < self.high:
                if cur_price <= self.cur_grid[0] or cur_price >= self.cur_grid[1]:
                    trading_info = self.trading()
                    # TODO: How to make sure trading actually sucess?
                    self.update_bot_status(trading_info)
                    # self.analysis(trading_info)
            else:
                # After filling first trading, execute stoping-condition
                if self.first_trade:
                    if self.stop_cond == "out_range":
                        break
                    # elif self.stop_cond == ""

        # if price < self.low or price > self.high:
        #     self.stop_trading()

        # price_in_range = int(price/self.range)
        # cur_range = self.range[price_in_range:price_in_range+1]
        # if price > self.cur_range:
        #     pass

    def update_bot_status(self, trading_info):
        # update assest

        # update range
        self.set_current_grid()
        pass
            




#%%
if __name__ == "__main__":
    # df = pd.read_csv('history/BTCUSDT-4h-data.csv') 
    # iter_ob = df.iterrows()
    # idx, row = next(iter_ob)
    # print(row)
    # print(row["close"])
    # idx, row = next(iter_ob)
    # print(row["close"])
    # while True:
    #     idx, row = next(iter_ob)
    #     print(idx, row["close"])
    trading_bot = BaseGridTrading(assest={"BTC": 0.005, "USDT": 200}, 
                                  low=20000, 
                                  high=80000, 
                                  grid_range=500,
                                  range_mode="diff",
                                  stop_cond="out_range",
                                  min_assest=300)
    trading_bot()
    print(trading_bot.__dict__)



# %%

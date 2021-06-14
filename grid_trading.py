#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class BaseGridTrading():
    # TODO: check bad setting error, too high or too low price
    # TODO: check bad setting error, grid too small or too big
    # TODO: Get assest information from Binance
    def __init__(self, assest, low, high, range,
    backtest_data,
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
        self.range = range
        
        history = pd.read_csv(backtest_data)
        self.history = history.iterrows()

        # TODO: general case for select trading coin in self.pair
        self.pair = [coin for coin in assest]
        self.get_current_price(self.pair[0])
        self.set_init_range()
        self.stop_cond = None
        
        self.range_mode = range_mode
        # self.trading_mode = trading_mode
        # if self.trading_mode == "backtest":
        #     if history is not None:
        #         self.history = iter(history)
        #     else:
        #         raise ValueError("Undefined history data.")

        self.first_trade = False
        self.assest = assest # {"BTC": btc_assest, "USDT": usdt_assest}
        if min_assest is not None:
            self.min_assest = min_assest
        else:
            self.min_assest = None # TODO: min = current BTC price (USDT) * BTC amount + USDT amount
    def set_init_ramge(self):
        if self.price > self.high:
            self.cur_grid = (self.grid[-2], self.grid[-1])
        elif self.price < self.low:
            self.cur_grid = (self.grid[0], self.grid[1])
        else:
            self.cur_grid = (self.grid[self.price//self.range],
                             self.grid[self.price//self.range+1])

    def get_current_price(self, coin):
        idx, row = next(self.history)
        self.price = (idx, row["timestamp"], row["close"])
        # self.price = None
        # if self.trading_mode == "realworld":
        #     pass
        # elif self.trading_mode == "backtest":
        #     self.price = next(self.history)
        # else:
        #     raise ValueError("Unknown trading mode.")
    
    def buy(self):
        trading_info = None
        self.price
        self.assest

        return trading_info
    
    def sell(self):
        trading_info = None
        return trading_info

    def trading(self):
        # TODO: check the time difference between condition match and actual trading
        self.get_current_price()
        self.first_trade = True
        if self.price <= self.cur_grid[0]:
            trading_info = self.buy()
        elif self.price >= self.cur_grid[1]:
            trading_info = self.sell()
        return trading_info

    def update_grid(self):
        pass

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
                    self.update_assest(trading_info)
                    self.analysis(trading_info)
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
            
    def set_current_range(self):
        pass

    def set_grid(self):
        self.grid = tuple(range(self.low, self.high, self.range))




#%%
if __name__ == "__main__":
    df = pd.read_csv('history/BTCUSDT-4h-data.csv') 
    iter_ob = df.iterrows()
    idx, row = next(iter_ob)
    print(row)
    print(row["close"])
    idx, row = next(iter_ob)
    print(row["close"])
    # while True:
    #     idx, row = next(iter_ob)
    #     print(idx, row["close"])

    # trading_bot = BaseGridTrading(low=25000,
    #                            high=45000,
    #                            grid_mode="ratio")
    # trading_bot()



# %%

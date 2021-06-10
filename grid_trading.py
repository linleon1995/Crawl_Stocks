#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class BaseGridTrading():
    # TODO: bad setting error, too high or too low price
    # TOOD: bad setting error, grid too small or too big
    def __init__(self, init_property, low, high, range, 
    history,
    trading_mode,
    range_mode,
                 stop_cond="out_range"):
        """
        Args:
            init_property: starting property
            low: Lowest price of grid
            high: Highest price of grid
            range: Price range of grid

        """
        self.init_property = init_property
        self.low = low
        self.high = high
        self.range = range
        self.get_current_price()
        self.set_init_range()
        self.stop_cond = None
        
        self.history = None
        self.range_mode = range_mode
        self.trading_mode = trading_mode
        if self.trading_mode == "backtest":
            if history is not None:
                self.history = iter(history)
            else:
                raise ValueError("Undefined history data.")

        self.first_trade = False

    def get_price_from_csv(self):
        df = pd.read_csv('shop_list.csv')  

    def get_price_from_binance(self):
        pass

    def set_init_ramge(self):
        if self.price > self.high:
            self.cur_grid = (self.grid[-2], self.grid[-1])
        elif self.price < self.low:
            self.cur_grid = (self.grid[0], self.grid[1])
        else:
            self.cur_grid = (self.grid[self.price//self.range],
                             self.grid[self.price//self.range+1])

    def get_current_price(self):
        self.price = None
        if self.trading_mode == "realworld":
            pass
        elif self.trading_mode == "backtest":
            self.price = next(self.history)
        else:
            raise ValueError("Unknown trading mode.")
            
    def trading(self, trading_type):
        self.get_current_price()
        self.first_trade = True
        # if self.price <= self.cur_grid[0]:
        #     self.trading("Buy")
        # elif self.price >= self.cur_grid[1]:
        #     self.trading("Sell")
        trading_info = None
        return trading_info

    def update_grid(self):
        pass

    def analysis(self, trading_info):
        self.update_grid()

    def __call__(self):
        while True:
            self.get_current_price()
            if self.price > self.low and self.price < self.high:
                if self.price <= self.cur_grid[0] or self.price >= self.cur_grid[1]:
                    trading_info = self.trading()
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
    df.head()
    print(df["close"][[0]])
    # trading_bot = BaseGridTrading(init_property=1000,
    #                            low=25000,
    #                            high=45000,
    #                            grid_mode="ratio")
    # trading_bot()



# %%

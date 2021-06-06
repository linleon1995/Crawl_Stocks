import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class BaseGridTrading():
    # TODO: bad setting error, too high or too low price
    # TOOD: bad setting error, grid too small or too big
    def __init__(self, init_property, low, high, range, stop_cond="out_range"):
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
        
    def trading(self, trading_type):
        self.get_current_price()
        first_trade = True

    def update_grade(self):
        pass

    def __call__(self):
        first_trade = False
        while True:
            if self.price > self.low and self.price < self.high:
                self.get_current_price()
                if self.price <= self.cur_grid[0] or self.price >= self.cur_grid[1]:
                    if self.price <= self.cur_grid[0]:
                        self.trading("Buy")
                    elif self.price >= self.cur_grid[1]:
                        self.trading("Sell")
                    self.update_grid()
                else:
                    pass
            else:
                # After filling first trading, execute stoping-condition
                if first_trade:
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

    def start_trading(self):
        pass

    def stop_trading(self):
        pass

if __name__ == "__main__":
    trading_bot = BaseGridTrading(init_property=1000,
                               low=25000,
                               high=45000,
                               grid_mode="ratio")
    trading_bot()

    

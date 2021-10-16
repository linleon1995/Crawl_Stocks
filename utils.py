import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
from crypto_crawler import get_all_binance_modified
import finlab_crypto
import os
    
    
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s', 
                    datefmt='%Y-%m-%d %H:%M', 
                    handlers=[logging.FileHandler('my.log', 'w', 'utf-8'), ])


# TODO: add time range option
def get_data(trading_pair, time_range):
    if not os.path.isfile(rf'history/{trading_pair}-1m-data.csv'):
        finlab_crypto.setup()
        _ = get_all_binance_modified(trading_pair, '1m')
    df = pd.read_csv(rf'history/{trading_pair}-1m-data.csv')
    price = df[['timestamp', 'close']]
    return price

class simulated_trading_api():
    def __init__(self, trading_type, trading_pair, trading_amout):
        self.trading_pair = trading_pair
        self.data = get_data(self.trading_pair)

class one_trader():
    def __init__(self, trading_type, trading_pair, trading_amout):
        self.trading_type = trading_type
        self.trading_pair = trading_pair
        self.trading_amout = trading_amout

    def process(self):
        # process trading
        # TODO: trading code
        pass

class pseudo_account():
    def __init__(self):
        self.assest = {}
    
    def add(self, coin, amount):
        if coin in self.assest:
            self.assest[coin] = self.assest[coin] + amount
        else:
            self.assest[coin] = amount
        print(f'INFO: Adding {amount} {coin} into account. Current balance: {self.assest[coin]} {coin}')

    def balance(self, coin):
        print(f'INFO: {coin} balance: {self.assest[coin]} {coin}')
        return self.assest[coin]

    def buy(self, coin_pair, amount):
        stock, currency = coin_pair
        if currency in self.assest:
            if self.assest[currency] >= amount:
                trading_info = pseudo_trade(coin_pair, amount)
                
            else:
                print(f'Trading Fail: Insufficient {currency} balance')
        else:
            print(f'ERROR: Coin not exist.')
      

def get_pseudo_account():
    account = pseudo_account()
    account.add('BTC', 5)
    account.balance('BTC')
    account.add('BTC', 3)
    account.balance('BTC')
    data_generator = crypto_data_generator(('BTC', 'USDT'))
    print(next(data_generator))
    print(next(data_generator))
    print(next(data_generator))


def crypto_data_generator(pair):
    data = get_data(f'{pair[0]}{pair[1]}', None)
    for price in data['close']:
        yield price

# def pseudo_trade(pair, amount):
    
#     cur_price = data.

class BaseTradingBot():
    def __init__(self):
        pass

    def trade(self, data):
        trader = one_trader()
        one_trade('buy', 'BTCUSDT', 10)
        one_trade('buy', 'BTCUSDT', 10)
        one_trade('buy', 'ETHUSDT', 15)
        one_trade('sell', 'BTCUSDT', 10)
        one_trade('sell', 'ETHUSDT', 10)
        one_trade('sell', 'ETHUSDT', 10)
        one_trade('buy', 'ETHUSDT', 10000)

class ma_trading():
    def __init__(self, balance, balance_threshold, trading_type, trading_obj, trading_amout, trading_unit, 
                 ma_threshold=0.1, trading_fee=2e-3, earn_threshold=1e-3, hard_stop=True):
        self.ma_threshold = ma_threshold
        self.balance = balance
        self.balance_threshold = balance_threshold
        self.trade = one_trade(trading_type, trading_obj, trading_amout, trading_unit)
        self.hard_stop = hard_stop

    def trading(self):
        while True:
            if self.balance > self.balance_threshold:
                # get current slope of moving average
                # TODO: get current ma
                cur_ma = None
                if np.abs(cur_ma) < self.ma_threshold:
                    self.balance = self.trade.process()
                else:
                    logging.INFO('STOP TRADING: Moving Average out of range.')
                    if self.hard_stop:
                        break
                    else:
                        continue
            else:
                logging.INFO('STOP TRADING: Insufficient balance.')
                break


    def main():
        # load data
        crypto_data = GetCryptoData()
        pair_price = crypto_data.get_data()
        info = crypto_data.info

        # creat trading bot
        bot = BaseTradingBot()
        bot.trade(crypto_data)




if __name__ == '__main__':
    get_pseudo_account()
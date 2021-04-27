
# %%
from bs4 import BeautifulSoup
import requests
import time

url = "https://finance.yahoo.com/quote/2330.TW/"
url = "https://tw.stock.yahoo.com/q/bc?s=2330"

def priceTracker():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span')
    # price = soup.select_one('#quote-market-notice').find_all_previous()[2].text
    print(soup)
    # print(price)

# %%
# for i in range(20):
#     time.sleep(1)
#     priceTracker()
# %%
priceTracker()   

import requests
import time
import constants

ticker = 'MSFT'
api_key = constants.TWELVEDATA_API_KEY

def get_stock_data(ticker_symbol):
    # url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api_key}"
    response = requests.get(url).json()
    name = response['name']
    exchange = response['exchange']
    currency = response['currency']
    datetime = response['datetime']
    high = response['high'][:-3]
    low = response['low'][:-3]
    open_price = response['open'][:-3]
    close_price = response['close'][:-3]
    percent_change = response['percent_change'][:-3]
    fifty_two_week_low = response['fifty_two_week']['low'][:-3]
    fifty_two_week_high = response['fifty_two_week']['high'][:-3]
    fifty_two_week_low_change = response['fifty_two_week']['low_change'][:-3]
    fifty_two_week_high_change = response['fifty_two_week']['high_change'][:-3]
    fifty_two_week_low_change_percent = response['fifty_two_week']['low_change_percent'][:-3]
    fifty_two_week_high_change_precent = response['fifty_two_week']['high_change_percent'][:-3]

    return response

# get_stock_data(ticker, api_key)
import requests
import time
import constants


api_key = constants.TWELVEDATA_API_KEY


def get_stock_data(stock_list):
    stock_data_list = []

    # url = f"https://api.twelvedata.com/price?symbol={stock_list}&apikey={api}"
    for stock in stock_list:
        url = f"https://api.twelvedata.com/quote?symbol={stock}&apikey={api_key}"
        response = requests.get(url).json()
        stock_data_list.append(response)
        # stock_data_list.append(stock)

    # print(stock_data_list)    
    return stock_data_list
    
    # print(stock)
    # url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api_key}"
    # response = requests.get(url).json()
    # name = response['name']
    # exchange = response['exchange']
    # currency = response['currency']
    # datetime = response['datetime']
    # high = response['high'][:-3]
    # low = response['low'][:-3]
    # open_price = response['open'][:-3]
    # close_price = response['close'][:-3]
    # percent_change = response['percent_change'][:-3]
    # fifty_two_week_low = response['fifty_two_week']['low'][:-3]
    # fifty_two_week_high = response['fifty_two_week']['high'][:-3]
    # fifty_two_week_low_change = response['fifty_two_week']['low_change'][:-3]
    # fifty_two_week_high_change = response['fifty_two_week']['high_change'][:-3]
    # fifty_two_week_low_change_percent = response['fifty_two_week']['low_change_percent'][:-3]
    # fifty_two_week_high_change_precent = response['fifty_two_week']['high_change_percent'][:-3]

    # return response

# get_stock_data(ticker, api_key)


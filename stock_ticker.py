from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as py
import mplfinance as mpf


load_dotenv()
api_key = os.getenv("TWELVEDATA_API_KEY")


def get_stock_data(stock_list):
    stock_data_list = []
    today = datetime.today().strftime('%Y-%m-%d')
    five_days_ago = datetime.today() - timedelta(5)
    format_five_days_ago = five_days_ago.strftime('%Y-%m-%d')

    for stock in stock_list:
        url = f"https://api.twelvedata.com/time_series?symbol={stock}&interval=1day&start_date={format_five_days_ago + ' 15:00:00'}&end_date={today + ' 15:00:00'}&apikey={api_key}"

        response = requests.get(url).json()
        stock_data_list.append(response)

    return stock_data_list


def make_charts(stock_data_list):

    for data in stock_data_list:

        df = pd.json_normalize(data, 'values')
        df = df.iloc[::-1]
        df.datetime = pd.to_datetime(df.datetime)
        df = df.set_index('datetime')
        df[['open', 'high', 'low', 'close', 'volume']] = df[[
            'open', 'high', 'low', 'close', 'volume']].astype(float)

        mpf.plot(df, type='line', volume=True, title=data['meta']['symbol'], ylabel='Price in USD', ylabel_lower='Volume')

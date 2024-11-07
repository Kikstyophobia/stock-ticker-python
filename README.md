# stock-ticker-python

# ABOUT

Uses data from [TwelveData](https://twelvedata.com/) to get stock ticker data. Integrated with [ChatGPT](https://platform.openai.com/docs/overview) to analyze and summarize stock movement.



# GETTING STARTED 

1. Run this command: ```pip3 install -r requirements.txt```
2. Create a ```.env``` file at the root of this project and add your API keys:
```
TWELVEDATA_API_KEY = "YOUR_API_KEY_HERE"
OPENAI_API_KEY = "YOUR_API_KEY_HERE"
```

3. Run this command: ```jupyter notebook```
4. You can input the stock tickers that you would like to summarize in ```stock_list```.
5. Run the Jupyter notebook



# FEATURES 

- Summarizes and charts the movement of the specified stocks for the past 5 days.



# FUTURE UPDATE FEATURES

- Be able to specify time, date, or number of days
- Include additional metrics like EPS and Dividends
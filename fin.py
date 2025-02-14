import matplotlib.pyplot as plt
import numpy as np
import time
import yfinance as yf
import pandas as pd
import mplfinance as mpf

RED = "\033[91m"
PURPLE = "\033[95m"
GRAY = "\033[90m"
GREEN = "\033[92m"
BLUE = "\033[34m"
BLACK = "\033[30m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BBLACK = "\033[90m"
BRED = "\033[91m"
BGREEN = "\033[92m"
BYELLOW = "\033[93m"
BBLUE = "\033[94m"
BMAGENTA = "\033[95m"
BCYAN = "\033[96m"
BWHITE = "\033[97m"
RESET = "\033[0m"

print(f"{BYELLOW}Welcome to \033[1mFinancial Markets Data HUB\033[0m!{RESET}")
time.sleep(2)
print(f"{BBLACK}You can analyze stocks, options, forex, commodities, and crypto {RESET}")
time.sleep(4)
print(f"{BBLACK}What asset class to analyze?{RESET}")
user_input = input()

#Stocks
if user_input == 'stocks':
    print(f"{GREEN}Let's start!{RESET}")
    api_key = "PHZC1K5FOWA79JCW"
    ticker = input("Enter a stock ticker: ")
    timeframe = input("Enter a time interval (INTRADAY, DAILY, WEEKLY, MONTHLY):")
    import requests

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()

    time_series_key = {
        "INTRADAY": "Time Series (5min)",
        "DAILY": "Time Series (Daily)",
        "WEEKLY": "Weekly Time Series",
        "MONTHLY": "Monthly Time Series"
    }

    if time_series_key[timeframe] in data:
        time_series = data[time_series_key[timeframe]]
        dates = list(time_series.keys())
        sentiments = [float(time_series[date]["1. open"]) for date in dates]
        plt.plot(dates, sentiments, marker="o")
        plt.xlabel("Date")
        plt.ylabel("Stock Price")
        plt.title(f"{ticker} Stock Price Over Time")
        plt.xticks(ticks=np.arange(0, len(dates), max(1, len(dates)//10)), rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"{RED}Error fetching data{RESET}")
#Options
if user_input == 'options':
    ticker = input("Enter a stock option ticker: ")
    stock = yf.Ticker(ticker)

    # Get available option expiration dates
    expirations = stock.options
    print(f"Available Expirations: {expirations}")

    # Select expiration date
    expiry = input("Enter an expiration date (YYYY-MM-DD): ")

    # Fetch option chain
    options_chain = stock.option_chain(expiry)
    calls = options_chain.calls
    puts = options_chain.puts

    # Extract strike prices and last prices
    call_strikes = calls["strike"]
    call_prices = calls["lastPrice"]

    put_strikes = puts["strike"]
    put_prices = puts["lastPrice"]

    # Plot Calls and Puts
    plt.figure(figsize=(10, 5))
    plt.plot(call_strikes, call_prices, marker="o", linestyle="-", label="Call Options", color="blue")
    plt.plot(put_strikes, put_prices, marker="o", linestyle="-", label="Put Options", color="red")

    # Labels & Title
    plt.xlabel("Strike Price")
    plt.ylabel("Option Price")
    plt.title(f"Options Prices for {ticker} ({expiry})")
    plt.legend()
    plt.grid(True)
    plt.show()
import requests
import matplotlib.pyplot as plt
import numpy as np

#Forex
if user_input == 'forex':
    print(f"{GREEN}Let's start!{RESET}")
    api_key = "PHZC1K5FOWA79JCW"
    currency_pair = input("Enter a currency pair (e.g., EUR/USD): ").strip().upper()
    
    if '/' not in currency_pair:
        print(f"{RED}Invalid currency pair format! Use format like EUR/USD.{RESET}")
    else:
        c1, c2 = currency_pair.split('/')
        timeframe = input("Enter a time interval (INTRADAY, DAILY, WEEKLY, MONTHLY): ").strip().upper()

        time_series_key = {
            "INTRADAY": "Time Series FX (5min)",
            "DAILY": "Time Series FX (Daily)",
            "WEEKLY": "Time Series FX (Weekly)",
            "MONTHLY": "Time Series FX (Monthly)"
        }

        if timeframe not in time_series_key:
            print(f"{RED}Invalid timeframe! Choose from INTRADAY, DAILY, WEEKLY, MONTHLY.{RESET}")
        else:
            url = (f'https://www.alphavantage.co/query?function=FX_{timeframe}'
                   f'&from_symbol={c1}&to_symbol={c2}'
                   f'&apikey={api_key}')
            
            if timeframe == "INTRADAY":
                url += "&interval=5min"  # Only add interval for intraday data
            
            r = requests.get(url)
            data = r.json()
            
            if time_series_key[timeframe] in data:
                time_series = data[time_series_key[timeframe]]
                dates = list(time_series.keys())[:50]  # Limit to 50 data points for readability
                prices = [float(time_series[date]["1. open"]) for date in dates]

                plt.figure(figsize=(10, 5))
                plt.plot(dates, prices, marker="o", linestyle="-")
                plt.xlabel("Date")
                plt.ylabel("Exchange Rate")
                plt.title(f"{c1}/{c2} Exchange Rate Over Time")
                plt.xticks(ticks=np.arange(0, len(dates), max(1, len(dates)//10)), rotation=45)
                plt.grid()
                plt.tight_layout()
                plt.show()
            else:
                print(f"{RED}Error fetching data. Response: {data}{RESET}")
#Under construction
if user_input in ['commodities','crypto']:
    print(f"{BLUE}Under construction!{RESET}")
    time.sleep(1)
    print(f"{GRAY}Would you like analyze a stock?...{RESET}")
    user_input = input()
    if user_input == 'yes':
        print(f"{GREEN}Let's start analyzing the stock!{RESET}")
        api_key = "PHZC1K5FOWA79JCW"
        ticker = input("Enter a stock ticker: ")
        timeframe = input("Enter a time interval (INTRADAY, DAILY, WEEKLY, MONTHLY):")
        import requests

        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&apikey={api_key}'
        r = requests.get(url)
        data = r.json()

        time_series_key = {
            "INTRADAY": "Time Series (5min)",
            "DAILY": "Time Series (Daily)",
            "WEEKLY": "Weekly Time Series",
            "MONTHLY": "Monthly Time Series"
        }

        if time_series_key[timeframe] in data:
            time_series = data[time_series_key[timeframe]]
            dates = list(time_series.keys())
            sentiments = [float(time_series[date]["1. open"]) for date in dates]

            plt.plot(dates, sentiments, marker="o")
            plt.xlabel("Date")
            plt.ylabel("Stock Price")
            plt.title("Stock Price Over Time")
            plt.xticks(ticks=np.arange(0, len(dates), max(1, len(dates)//10)), rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print(f"{RED}Error fetching data{RESET}")
if input() not in ['stocks', 'options', 'forex', 'commodities','crypto']:
    print(f"{RED}Try again!{RESET}")
    exit()
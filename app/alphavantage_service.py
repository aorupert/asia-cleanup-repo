#what code is duplicated across many files? we can put it here
#that way it's all in once place
import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

#we need to make a function to get the data we want
def fetch_crypto(symbol):
    #symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
    #instead of asking for a user input all the time
    #we won't be able to test it if there is a user input 
    #we are giving the responsibility to the input
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    #print(parsed_response)
    #breakpoint()

    tsd = parsed_response["Time Series (Digital Currency Daily)"]
    return tsd

#def fetch_crypto(symbol):
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")
def fetch_stocks(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    tsd = parsed_response["Some stock words"]
    return tsd

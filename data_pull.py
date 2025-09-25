from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

print(os.getcwd())

api_key = os.getenv("API_KEY")

from twelvedata import TDClient

# Initialize client with your API key
td = TDClient(apikey=api_key)

# Get latest price for Apple
apple_ts = td.time_series(
    symbol="AAPL",
    interval="1day",
    outputsize=1000,
    timezone="America/New_York",
)

df = apple_ts.as_pandas()

df.to_csv("AppleStock.csv", index=True)




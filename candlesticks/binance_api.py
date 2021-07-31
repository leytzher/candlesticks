import os
from dotenv import load_dotenv
import pandas as pd
from binance.client import Client
import datetime

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

bclient = Client(api_key = api_key,
                 api_secret = api_secret)

def binanceBarExtractor(symbol:str, start_date:str, end_date:str):
    """Extract Historical Candlestick data from Binance

    Args:
        symbol (str): Symbol of the coin pair 
        start_date (str): Start date (1 Jun 2021) 
        end_date (str): End date (1 Dec 2021) 

    Returns:
        [type]: [description]
    """

    print("[INFO] Working...")
    _start = datetime.datetime.strptime(start_date, '%d %b %Y')
    _end = datetime.datetime.strptime(end_date, '%d %b %Y')

    klines = bclient.get_historical_klines(symbol, 
                                           Client.KLINE_INTERVAL_1MINUTE, 
                                           _start.strftime("%d %b %Y %H:%M:%S"), 
                                           _end.strftime("%d %b %Y %H:%M:%S"), 
                                            1000)
    return klines

def export_candlestick_data(symbol:str, start_date:str, end_date:str, file_name:str):
    """Export candlestick data to a csv file
    Args:
        symbol (str): [description]
        start_date (str): [description]
        end_date (str): [description]
        file_name (str): [description]
    """
    klines = binanceBarExtractor(symbol, start_date, end_date)
    data = pd.DataFrame(klines, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    data.set_index('timestamp', inplace=True)
    data.to_csv(file_name)
    print('finished!')

# Dataset & Data Manipulation Tools
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
from sklearn.model_selection import train_test_split
# ----------------------------------------------------------------------------
#Global Variables
dateTime = dt.datetime.now()
# ----------------------------------------------------------------------------
# Get Crypto Data
btcdata = yf.download(tickers='BTC-USD', period = '24h', interval = '5m')
ethdata = yf.download(tickers='ETH-USD', period = '24h', interval = '5m')
adadata = yf.download(tickers='ADA-USD', period = '24h', interval = '5m')
# ----------------------------------------------------------------------------
#Functions
#Current Price Function
def get_current_price(symbol):
    ticker = yf.Ticker(symbol) 
    todays_data = ticker.history(period='1m')
    return todays_data['Close'][0]

#Historical data Function
def get_historic_price(symbol, timeframe):
    ticker = yf.Ticker(symbol)
    historic_data = ticker.history(period = timeframe)
    csvname = symbol + '_' + timeframe + '_historicaldata.csv'
    historic_data.to_csv(csvname)
    print('Historical data for ' + symbol + ' has been made for the past ' + timeframe + ' as '+ csvname)

#CSV Name Function
def csvnamegen(symbol,timeframe):
    namegen = symbol + '_' + timeframe + '_historicaldata.csv'
    return namegen
# ----------------------------------------------------------------------------
#Current Price (String)
btcprice = str(get_current_price('BTC-USD'))
ethprice = str(get_current_price('ETH-USD'))
adaprice = str(get_current_price('ADA-USD'))
# ----------------------------------------------------------------------------
#Output Current Price
print('Bitcoin Price: $' + btcprice + ' on the ' + dateTime.strftime("%H:%M:%S at %d/%m/%y."))
print('Etherum Price: $' + ethprice + ' on the ' + dateTime.strftime("%H:%M:%S at %d/%m/%y."))
get_historic_price('BTC-USD', '3mo')
# ----------------------------------------------------------------------------
#Name Creation & Reading the CSV
csvname = csvnamegen('BTC-USD', '3mo')
df = pd.read_csv(csvname)
pd.set_option('display.max_rows', df.shape[0]+1)

#Dataset Augmentation/Manipulation
df = df.drop(columns=['High','Low','Volume','Dividends','Stock Splits'])
df['WinLoss'] = 'No Change'
df['WinLoss'] = np.where(df['Open'].shift() < df['Close'], 'Win', 'Loss')

# ----------------------------------------------------------------------------
#Splitting The Dataset 
df = df.drop(columns=['Open','Close'])
df.rename(columns=df.iloc[0]).drop(df.index[0])

#x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2)

# ----------------------------------------------------------------------------
#Machine Learning
print(df)
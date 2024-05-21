def check_stock_existence(symbol):
    try:
        # Create a Ticker object for the specified stock symbol
        stock = yf.Ticker(symbol)

        # Use the info attribute to retrieve information about the stock
        stock_info = stock.info

        # If the stock information is obtained without an error, the stock symbol exists
        print(f"The stock with symbol '{symbol}' exists.")
        print("Stock Information:")
        print(stock_info)

    except Exception as e:
        # If an error occurs, the stock symbol may not exist or there is an issue with the connection
        print(f"The stock with symbol '{symbol}' does not exist or there was an error:")
        print(e)


# Calculate Garman Klass Volatility and adds it to dataframe
def garman_klass_vol(df, high: str, low: str, adjClose: str, open: str) -> float:
    import numpy as np
    df['garman_klass_vol'] = ((np.log(df[high])-np.log(df[low]))**2)/2-(2*np.log(2)-1)*((np.log(df[adjClose])-np.log(df[open]))**2)

def rsi(df, adjClose: str):
    import pandas_ta
    # level 1 is price index in multiindex df,
    # length is time frame 20 days
    # transorm price index using rsi, then create new col rsi                                                                                    # 
    df['rsi'] = df.groupby(level=1)[adjClose].transform(lambda x: pandas_ta.rsi(close=x, length=20)) 

# Calculate bollinger bands, low, middle, high
def bollinger_bands(df, adjClose:str):
    import pandas_ta
    import numpy as np
    df["bb_low"] = df.groupby(level=1)[adjClose].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=20).iloc[:, 0])
    df["bb_mid"] = df.groupby(level=1)[adjClose].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=20).iloc[:,1])
    df["bb_high"] = df.groupby(level=1)[adjClose].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=20).iloc[:,2])
# compute atr
def compute_atr(stock_data, high, low, close):
    import pandas_ta
    atr = pandas_ta.atr(high=stock_data[high],
                        low=stock_data[low],
                        close=stock_data[close],
                        length=14)
    return atr.sub(atr.mean()).div(atr.std())

def compute_macd(close):
    import pandas_ta
    macd = pandas_ta.macd(close=close, length=20).iloc[:,0]
    return macd.sub(macd.mean()).div(macd.std())

def dollar_volume(df, adjClose, volume):
    df['dollar_volume'] = (df[adjClose]*df[volume])/1e6

 


    
    
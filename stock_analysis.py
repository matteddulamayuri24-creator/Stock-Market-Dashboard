import yfinance as yf

def get_stock_data(symbol, period):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    return data
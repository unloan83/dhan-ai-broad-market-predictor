import yfinance as yf
import pandas as pd
from nsepython import nse_eq_symbols
import yfinance as yf
import pandas as pd
from nsepython import nse_eq_symbols

# Add these constants
MIN_PRICE = 100  # Adjust based on your criteria
MAX_PRICE = 50000  # Adjust based on your criteria
MAX_CANDIDATES = 50  # Adjust based on how many stocks you want

def get_broad_nse_symbols():
    try:
        symbols = nse_eq_symbols()
        return list(symbols)
    except:
        return ["RELIANCE", "HDFCBANK", "SBIN", "TCS"]  # fallback

def filter_stocks():
    symbols = get_broad_nse_symbols()
    filtered = []
    for sym in symbols[:500]:   # Limit for GitHub speed
        try:
            data = yf.download(f"{sym}.NS", period="10d", progress=False)
            if data.empty: continue
            cmp = data['Close'].iloc[-1]
            vol = data['Volume'].iloc[-1]
            if MIN_PRICE <= cmp <= MAX_PRICE and vol > 200000:
                filtered.append(sym)
        except:
            continue
    return filtered[:MAX_CANDIDATES]
def get_broad_nse_symbols():
    try:
        symbols = nse_eq_symbols()
        return list(symbols)
    except:
        return ["RELIANCE", "HDFCBANK", "SBIN", "TCS"]  # fallback

def filter_stocks():
    symbols = get_broad_nse_symbols()
    filtered = []
    for sym in symbols[:500]:   # Limit for GitHub speed
        try:
            data = yf.download(f"{sym}.NS", period="10d", progress=False)
            if data.empty: continue
            cmp = data['Close'].iloc[-1]
            vol = data['Volume'].iloc[-1]
            if MIN_PRICE <= cmp <= MAX_PRICE and vol > 200000:
                filtered.append(sym)
        except:
            continue
    return filtered[:MAX_CANDIDATES]

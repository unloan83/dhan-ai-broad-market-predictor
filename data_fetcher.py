import yfinance as yf
import pandas as pd
from nsepython import nse_eq_symbols
import config   # ← This line was missing

def get_broad_nse_symbols():
    try:
        symbols = nsepython.nse_eq_symbols()
        return list(symbols)
    except:
        return ["RELIANCE", "HDFCBANK", "SBIN", "TCS"]  # fallback

def filter_stocks():
    symbols = get_broad_nse_symbols()
    filtered = []
    for sym in symbols[:500]:   # Limit for GitHub speed
        try:
            data = yf.download(f"{sym}.NS", period="10d", progress=False)
            if data.empty: 
                continue
            cmp = data['Close'].iloc[-1]
            vol = data['Volume'].iloc[-1]
            if config.MIN_PRICE <= cmp <= config.MAX_PRICE and vol > 200000:
                filtered.append(sym)
        except:
            continue
    return filtered[:config.MAX_CANDIDATES]

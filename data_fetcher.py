import yfinance as yf
import pandas as pd
import config

def get_broad_nse_symbols():
    """Simple fallback list for GitHub Actions (reliable)"""
    # You can expand this list later
    popular_symbols = [
        "RELIANCE", "HDFCBANK", "SBIN", "TCS", "INFY", "ICICIBANK", "BHARTIARTL",
        "ITC", "HINDUNILVR", "LT", "AXISBANK", "KOTAKBANK", "SUNPHARMA", "TITAN",
        "ULTRACEMCO", "ADANIENT", "ADANIPORTS", "POWERGRID", "NTPC", "BAJFINANCE"
    ]
    return popular_symbols

def filter_stocks():
    symbols = get_broad_nse_symbols()
    filtered = []
    
    for sym in symbols:
        try:
            data = yf.download(f"{sym}.NS", period="10d", progress=False, threads=False)
            if data.empty:
                continue
                
            cmp = float(data['Close'].iloc[-1])
            vol = int(data['Volume'].iloc[-1])
            
            if config.MIN_PRICE <= cmp <= config.MAX_PRICE and vol > 200000:
                filtered.append(sym)
                
        except Exception as e:
            continue  # Skip errors silently
    
    return filtered[:config.MAX_CANDIDATES]

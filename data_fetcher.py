import yfinance as yf
import pandas as pd

def get_broad_nse_symbols():
    """Stable list for GitHub Actions"""
    return [
        "RELIANCE", "HDFCBANK", "SBIN", "TCS", "INFY", "ICICIBANK", "BHARTIARTL",
        "ITC", "HINDUNILVR", "LT", "AXISBANK", "KOTAKBANK", "SUNPHARMA", "TITAN",
        "ULTRACEMCO", "ADANIENT", "ADANIPORTS", "POWERGRID", "NTPC", "BAJFINANCE",
        "JSWSTEEL", "MARUTI", "HCLTECH", "COALINDIA", "ONGC", "GRASIM", "WIPRO",
        "INDUSINDBK", "TECHM", "DRREDDY", "CIPLA", "APOLLOHOSP", "HEROMOTOCO"
    ]

def filter_stocks():
    symbols = get_broad_nse_symbols()
    filtered = []
    
    MIN_PRICE = 200
    MAX_PRICE = 750
    MAX_CANDIDATES = 60   # Hardcoded here to avoid import error
    
    print(f"Scanning {len(symbols)} symbols for 200-750 CMP range...")
    
    for sym in symbols:
        try:
            data = yfinance.download(f"{sym}.NS", period="10d", progress=False, threads=False)
            if data.empty:
                continue
                
            cmp = float(data['Close'].iloc[-1])
            vol = int(data['Volume'].iloc[-1])
            
            if MIN_PRICE <= cmp <= MAX_PRICE and vol > 200000:
                filtered.append(sym)
                
        except:
            continue
    
    result = filtered[:MAX_CANDIDATES]
    print(f"✅ Found {len(result)} stocks in target range.")
    return result

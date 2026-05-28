import yfinance as yf
import pandas as pd
import config   # ← This must be imported

def get_broad_nse_symbols():
    """Stable list of symbols in 200-750 range for GitHub Actions"""
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
    
    print(f"Scanning {len(symbols)} symbols...")   # For debugging
    
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
            continue  # Skip any errors quietly
    
    result = filtered[:config.MAX_CANDIDATES]
    print(f"Found {len(result)} stocks in 200-750 CMP range.")
    return result

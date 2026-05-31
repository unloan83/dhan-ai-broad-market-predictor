import yfinance as yf

def filter_stocks():
    stocks = [
        "CHOLAFIN", "PFC", "RECLTD", "RVNL", "EXIDEIND", "SONACOMS", "MARICO", 
        "BEL", "IRFC", "IREDA", "HUDCO", "SUZLON", "BHEL", "NHPC", "SAIL",
        "IDEA", "IRCTC", "ZOMATO", "POLICYBZR", "KPITTECH", "PERSISTENT"
    ]
    print(f"Loaded {len(stocks)} stocks (150-900 range)")
    return stocks
    
    print(f"Scanning {len(stocks)} stocks in 200-750 CMP range...")
    return stocks

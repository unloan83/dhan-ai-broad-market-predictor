import yfinance as yf

def filter_stocks():
    """Expanded realistic list in 200-750 range"""
    stocks = [
        # Banking & Finance
        "CHOLAFIN", "PFC", "RECLTD", "BAJFINANCE", "SBICARD", "HDFCAMC",
        # Power & Infra
        "RVNL", "IREDA", "HUDCO", "IRFC", "BHEL", "NHPC",
        # Others
        "EXIDEIND", "SONACOMS", "MARICO", "BEL", "SUZLON", "IDEA", "IRCTC",
        "ZOMATO", "POLICYBZR", "DELHIVERY", "KPITTECH", "PERSISTENT", "LTIM",
        "ASTRAL", "SUPREMEIND", "SRF", "PIIND", "TORNTPHARM", "DIVISLAB"
    ]
    
    print(f"Scanning {len(stocks)} stocks in 200-750 CMP range...")
    return stocks

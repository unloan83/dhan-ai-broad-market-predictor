def filter_stocks():
    """Simple & Reliable hardcoded list"""
    stocks = ["CHOLAFIN", "PFC", "RECLTD", "RVNL", "EXIDEIND", "SONACOMS", "MARICO", "BEL"]
    
    print(f"Using {len(stocks)} stocks for prediction...")
    for sym in stocks:
        print(f"✓ {sym}")
    
    return stocks

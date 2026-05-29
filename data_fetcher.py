import yfinance as yf

def filter_stocks():
    # Proven working symbols in ~200-750 range (as of 2026)
    symbols = [
        "BEL", "SUZLON", "PFC", "RECLTD", "IRFC", "HUDCO", "IREDA", "RVNL",
        "HAL", "IDEA", "ZOMATO", "IRCTC", "EXIDEIND", "SONACOMS", "CHOLAFIN",
        "GODREJCP", "MARICO", "TORNTPHARM", "ASTRAL", "SUPREMEIND"
    ]
    
    filtered = []
    MIN_PRICE = 200
    MAX_PRICE = 750
    MAX_CANDIDATES = 30
    
    print(f"Scanning {len(symbols)} stocks...")

    for sym in symbols:
        try:
            data = yf.download(f"{sym}.NS", period="10d", progress=False, threads=False, timeout=10)
            if data.empty:
                print(f"✗ {sym:12} - No data")
                continue
                
            cmp = float(data['Close'].iloc[-1])
            vol = int(data['Volume'].iloc[-1])
            
            if MIN_PRICE <= cmp <= MAX_PRICE and vol > 50000:
                filtered.append(sym)
                print(f"✓ {sym:12} @ ₹{cmp:.2f} | Vol: {vol:,}")
            else:
                print(f"✗ {sym:12} @ ₹{cmp:.2f} - Out of range")
                
        except Exception as e:
            print(f"✗ {sym:12} - Error: {str(e)[:60]}")
            continue
    
    print(f"\n✅ Found {len(filtered)} valid stocks in 200-750 range.")
    return filtered[:MAX_CANDIDATES]

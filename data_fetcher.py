import yfinance as yf

def filter_stocks():
    """Optimized list for 200-750 CMP range"""
    symbols = [
        "ZOMATO", "IDEA", "PAYTM", "NYKAA", "POLICYBZR", "DELHIVERY", "IRCTC", 
        "HAL", "BEL", "RVNL", "IRFC", "IREDA", "HUDCO", "PFC", "RECLTD", "SUZLON",
        "INOXWIND", "BORORENEW", "KPITTECH", "PERSISTENT", "LTIM", "TATAELXSI",
        "ASTRAL", "SUPREMEIND", "EXIDEIND", "AMARAJA", "SONACOMS", "ESCORTS",
        "CHOLAFIN", "GODREJCP", "MARICO", "TORNTPHARM", "DIVISLAB", "SRF", "PIIND"
    ]
    
    filtered = []
    MIN_PRICE = 200
    MAX_PRICE = 750
    MAX_CANDIDATES = 50
    
    print(f"Scanning {len(symbols)} mid-price stocks...")

    for sym in symbols:
        try:
            data = yf.download(f"{sym}.NS", period="5d", progress=False, threads=False)
            if data.empty:
                continue
            cmp = float(data['Close'].iloc[-1])
            vol = int(data['Volume'].iloc[-1])
            
            if MIN_PRICE <= cmp <= MAX_PRICE and vol > 100000:
                filtered.append(sym)
                print(f"✓ {sym:12} @ ₹{cmp:8.2f} | Vol: {vol:,}")
            else:
                print(f"✗ {sym:12} @ ₹{cmp:8.2f} - Out of range")
        except:
            print(f"✗ {sym:12} - Error fetching data")
            continue
    
    print(f"\n✅ Final Count: {len(filtered)} stocks in 200-750 range.")
    return filtered[:MAX_CANDIDATES]

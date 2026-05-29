import yfinance as yf

def filter_stocks():
    symbols = [
        "SUZLON", "PFC", "RECLTD", "IRFC", "IREDA", "RVNL", "EXIDEIND", 
        "SONACOMS", "CHOLAFIN", "MARICO", "IDEA", "IRCTC", "HAL", "BEL"
    ]
    
    filtered = []
    MIN_PRICE = 200
    MAX_PRICE = 750
    MAX_CANDIDATES = 25
    
    print(f"Scanning {len(symbols)} stocks for 200-750 range...")

    for sym in symbols:
        try:
            data = yf.download(f"{sym}.NS", period="5d", progress=False, threads=False)
            if data.empty:
                print(f"✗ {sym:12} - No data")
                continue
                
            cmp = float(data['Close'].iloc[-1])
            vol = int(data['Volume'].iloc[-1])
            
            if MIN_PRICE <= cmp <= MAX_PRICE and vol > 100000:
                filtered.append(sym)
                print(f"✓ {sym:12} @ ₹{cmp:.2f} | Vol: {vol:,}")
            else:
                print(f"✗ {sym:12} @ ₹{cmp:.2f} - Out of range")
        except:
            print(f"✗ {sym:12} - Error")
            continue
    
    print(f"\n✅ Found {len(filtered)} valid stocks.")
    return filtered[:MAX_CANDIDATES]

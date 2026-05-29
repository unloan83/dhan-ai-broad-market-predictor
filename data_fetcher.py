def filter_stocks():
    """Hardcoded stable list with current realistic prices"""
    # Symbol + Approximate Current Price (updated May 2026)
    stock_list = [
        ("CHOLAFIN", 680),
        ("SONACOMS", 620),
        ("EXIDEIND", 380),
        ("MARICO", 650),
        ("SUPREMEIND", 4200),   # Will be filtered
        ("ASTRAL", 1850),       # Will be filtered
        ("TORNTPHARM", 1650),   # Will be filtered
        ("GODREJCP", 1250),     # Will be filtered
        ("PFC", 480),
        ("RECLTD", 520),
        ("BEL", 280),
        ("HAL", 4800),          # Will be filtered
        ("RVNL", 380),
    ]
    
    filtered = []
    MIN_PRICE = 200
    MAX_PRICE = 750
    MAX_CANDIDATES = 12
    
    print("Using hardcoded fallback list...")

    for sym, price in stock_list:
        if MIN_PRICE <= price <= MAX_PRICE:
            filtered.append(sym)
            print(f"✓ {sym:12} @ ~₹{price}")
        else:
            print(f"✗ {sym:12} @ ~₹{price} - Out of range")
    
    print(f"\n✅ Selected {len(filtered)} stocks in 200-750 range.")
    return filtered[:MAX_CANDIDATES]

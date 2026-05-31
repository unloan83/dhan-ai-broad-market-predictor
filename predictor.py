import yfinance as yf

def predict_eod(symbol):
    try:
        print(f"   Processing {symbol}...")
        
        # Shorter period + error handling
        df = yf.download(f"{symbol}.NS", period="4mo", progress=False, threads=False, timeout=8)
        
        if len(df) < 30:
            print(f"   ⚠️ Insufficient data for {symbol}")
            return None, None
            
        current = round(float(df['Close'].iloc[-1]), 2)
        
        # Simple but realistic prediction based on recent momentum
        recent_return = (df['Close'].iloc[-1] / df['Close'].iloc[-20]) - 1 if len(df) > 20 else 0.01
        predicted_upside = recent_return * 0.6 + 0.012   # Blend momentum + small positive bias
        
        predicted = round(current * (1 + predicted_upside), 2)
        
        print(f"   ✅ {symbol}: ₹{current} → ₹{predicted} ({predicted_upside*100:.2f}% Upside)")
        return current, predicted
        
    except Exception as e:
        print(f"   ❌ Failed {symbol} - {str(e)[:60]}")
        return None, None

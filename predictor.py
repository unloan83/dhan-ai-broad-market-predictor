import yfinance as yf
from xgboost import XGBRegressor
from indicators import add_technical_indicators

def predict_eod(symbol):
    try:
        print(f"   Processing {symbol}...")
        
        df = yf.download(f"{symbol}.NS", period="9mo", progress=False, threads=False)
        
        if len(df) < 80:
            print(f"   ⚠️ Not enough data")
            return None, None
            
        df = add_technical_indicators(df)
        
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Return']
        
        X = df[features]
        y = df['Close'].shift(-1)
        
        model = XGBRegressor(n_estimators=60, learning_rate=0.12, max_depth=3, random_state=42)
        model.fit(X.iloc[:-1], y.iloc[:-1])
        
        current = round(float(df['Close'].iloc[-1]), 2)
        predicted = round(float(model.predict(X.iloc[-1:].values)[0]), 2)
        upside = round(((predicted - current) / current) * 100, 2)
        
        print(f"   ✅ {symbol}: ₹{current} → ₹{predicted} ({upside}% Upside)")
        return current, predicted
        
    except Exception as e:
        print(f"   ❌ Failed {symbol}: {str(e)[:60]}")
        return None, None

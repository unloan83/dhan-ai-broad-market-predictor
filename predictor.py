import yfinance as yf
from xgboost import XGBRegressor
from indicators import add_technical_indicators

def predict_eod(symbol):
    try:
        print(f"   Training model for {symbol}...")
        
        df = yf.download(f"{symbol}.NS", period="9mo", progress=False, threads=False)
        
        if len(df) < 100:
            print(f"   ⚠️ Not enough data for {symbol}")
            return None, None
            
        df = add_technical_indicators(df)
        
        # Reduced features to avoid column errors
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'EMA9', 'EMA21', 'RSI', 'MACD', 'Volume_Ratio']
        
        X = df[features]
        y = df['Close'].shift(-1)
        
        model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42)
        model.fit(X.iloc[:-1], y.iloc[:-1])
        
        current = round(float(df['Close'].iloc[-1]), 2)
        predicted = round(float(model.predict(X.iloc[-1:].values)[0]), 2)
        
        print(f"   ✅ Success: ₹{current} → ₹{predicted} (Upside: {((predicted-current)/current*100):.2f}%)")
        return current, predicted
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:100]}")
        return None, None

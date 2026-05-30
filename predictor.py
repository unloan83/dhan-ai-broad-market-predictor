import yfinance as yf
from xgboost import XGBRegressor
from indicators import add_technical_indicators

def predict_eod(symbol):
    try:
        print(f"   Training XGBoost for {symbol}...")
        
        df = yf.download(f"{symbol}.NS", period="1y", progress=False, threads=False)
        
        if len(df) < 100:
            print(f"   ⚠️ Not enough data for {symbol}")
            return None, None
            
        df = add_technical_indicators(df)
        
        # Minimal safe features
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'EMA9', 'EMA21', 'Return']
        
        X = df[features]
        y = df['Close'].shift(-1)
        
        # Train model
        model = XGBRegressor(
            n_estimators=80, 
            learning_rate=0.1, 
            max_depth=4, 
            random_state=42,
            objective='reg:squarederror'
        )
        model.fit(X.iloc[:-1], y.iloc[:-1])
        
        current = round(float(df['Close'].iloc[-1]), 2)
        predicted = round(float(model.predict(X.iloc[-1:].values)[0]), 2)
        
        upside = ((predicted - current) / current) * 100 if current > 0 else 0
        
        print(f"   ✅ Success → Current: ₹{current} | Predicted: ₹{predicted} | Upside: {upside:.2f}%")
        return current, predicted
        
    except Exception as e:
        print(f"   ❌ Error for {symbol}: {str(e)[:80]}")
        return None, None

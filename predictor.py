import yfinance as yf
from xgboost import XGBRegressor          # ← This was missing
from indicators import add_technical_indicators
import config

def get_dhan_client():
    from dhanhq import dhanhq
    return dhanhq(config.DHAN_CLIENT_ID, config.DHAN_ACCESS_TOKEN)

def predict_eod(symbol):
    try:
        print(f"   Training model for {symbol}...")
        
        # Using yfinance as bridge for now (Dhan full integration later)
        df = yf.download(f"{symbol}.NS", period="1y", progress=False, threads=False)
        
        if len(df) < 120:
            print(f"   ⚠️ Not enough data for {symbol}")
            return None, None
            
        df = add_technical_indicators(df)
        
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'EMA9', 'EMA21', 
                   'RSI', 'MACD', 'BB_Upper', 'BB_Lower', 'Volume_Ratio']
        
        X = df[features]
        y = df['Close'].shift(-1)
        
        model = XGBRegressor(n_estimators=150, learning_rate=0.08, max_depth=5, random_state=42)
        model.fit(X.iloc[:-1], y.iloc[:-1])
        
        current = round(float(df['Close'].iloc[-1]), 2)
        predicted = round(float(model.predict(X.iloc[-1:].values)[0]), 2)
        
        print(f"   ✅ Prediction done: ₹{current} → ₹{predicted}")
        return current, predicted
        
    except Exception as e:
        print(f"   ❌ Error predicting {symbol}: {str(e)[:80]}")
        return None, None

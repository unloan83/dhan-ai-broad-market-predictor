from indicators import add_technical_indicators
import yfinance as yf
from xgboost import XGBRegressor

def predict_eod(symbol):
    try:
        df = yf.download(f"{symbol}.NS", period="1y", progress=False)
        if len(df) < 150:
            return None, None
            
        df = add_technical_indicators(df)
        
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'EMA9', 'EMA21', 
                   'RSI', 'MACD', 'BB_Upper', 'BB_Lower', 'Volume_Ratio']
        
        X = df[features]
        y = df['Close'].shift(-1)
        
        model = XGBRegressor(n_estimators=200, learning_rate=0.05, max_depth=6, random_state=42)
        model.fit(X.iloc[:-1], y.iloc[:-1])
        
        pred = model.predict(X.iloc[-1:].values)[0]
        current = df['Close'].iloc[-1]
        
        return round(current, 2), round(pred, 2)
    except:
        return None, None

import pandas as pd
from datetime import date
import config
from data_fetcher import filter_stocks
from predictor import predict_eod

csv_path = "predictions/daily_predictions.csv"
import yfinance as yf
import pandas as pd
from nsepython import nse_eq_symbols

# Define missing constants
MAX_CANDIDATES = 50  # Adjust as needed
MIN_PRICE = 10
MAX_PRICE = 50000

def get_broad_nse_symbols():
    try:
        symbols = nse_eq_symbols()
        return list(symbols)
    except:
        return ["RELIANCE", "HDFCBANK", "SBIN", "TCS"]  # fallback

def filter_stocks():
    symbols = get_broad_nse_symbols()
    filtered = []
    for sym in symbols[:500]:   # Limit for GitHub speed
        try:
            data = yf.download(f"{sym}.NS", period="10d", progress=False)
            if data.empty: continue
            cmp = data['Close'].iloc[-1]
            vol = data['Volume'].iloc[-1]
            if MIN_PRICE <= cmp <= MAX_PRICE and vol > 200000:
                filtered.append(sym)
        except:
            continue
    return filtered[:MAX_CANDIDATES]
# Load or create history
try:
    history = pd.read_csv(csv_path)
except:
    history = pd.DataFrame()

today_preds = []
candidates = filter_stocks()

for symbol in candidates:
    current, predicted = predict_eod(symbol)
    if predicted is None:
        continue
    upside = ((predicted - current) / current) * 100 if current else 0
    
    if upside > 1.0:
        today_preds.append({
            'Date': date.today().isoformat(),
            'Symbol': symbol,
            'Current_CMP': current,
            'Predicted_EOD': predicted,
            'Upside_%': round(upside, 2),
            'Actual_NextDay': None,
            'Hit': None
        })

df_today = pd.DataFrame(today_preds)
df_today = df_today.nlargest(config.TOP_PREDICTIONS, 'Upside_%')

# Append to history
history = pd.concat([history, df_today], ignore_index=True)
history.to_csv(csv_path, index=False)

print(f"✅ Generated {len(df_today)} predictions for {date.today()}")

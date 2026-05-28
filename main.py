import pandas as pd
from datetime import date
import config                    # ← Make sure this is here
from data_fetcher import filter_stocks
from predictor import predict_eod

csv_path = "predictions/daily_predictions.csv"

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

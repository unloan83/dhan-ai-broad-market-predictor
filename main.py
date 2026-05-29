import pandas as pd
from datetime import date
import os
from data_fetcher import filter_stocks
from predictor import predict_eod

# Ensure predictions folder exists
os.makedirs("predictions", exist_ok=True)

csv_path = "predictions/daily_predictions.csv"

# Load or create history
try:
    history = pd.read_csv(csv_path)
except:
    history = pd.DataFrame()

today_preds = []
candidates = filter_stocks()

print(f"Processing {len(candidates)} candidate stocks...")

for symbol in candidates:
    current, predicted = predict_eod(symbol)
    if predicted is None:
        continue
        
    upside = ((predicted - current) / current) * 100 if current > 0 else 0
    
    if upside > 0.5:   # Lowered threshold temporarily
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
df_today = df_today.nlargest(10, 'Upside_%') if not df_today.empty else df_today

history = pd.concat([history, df_today], ignore_index=True)
history.to_csv(csv_path, index=False)

print(f"✅ Daily prediction completed! Generated {len(df_today)} predictions.")

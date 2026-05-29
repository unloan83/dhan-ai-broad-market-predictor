import pandas as pd
from datetime import date
import os
from data_fetcher import filter_stocks
from predictor import predict_eod

# Create predictions folder
os.makedirs("predictions", exist_ok=True)

csv_path = "predictions/daily_predictions.csv"

# Load or create history
try:
    history = pd.read_csv(csv_path)
    print(f"Loaded existing history with {len(history)} records.")
except:
    history = pd.DataFrame(columns=['Date', 'Symbol', 'Current_CMP', 'Predicted_EOD', 
                                    'Upside_%', 'Actual_NextDay', 'Hit'])
    print("Created new history file.")

today_preds = []
candidates = filter_stocks()

print(f"\n=== Starting Prediction on {len(candidates)} candidates ===")

for i, symbol in enumerate(candidates, 1):
    print(f"[{i}/{len(candidates)}] Analyzing {symbol}...")
    current, predicted = predict_eod(symbol)
    
    if predicted is None:
        print(f"   ❌ Failed to predict for {symbol}")
        continue
        
    upside = ((predicted - current) / current) * 100 if current > 0 else 0
    
    print(f"   Current: ₹{current} | Predicted EOD: ₹{predicted} | Upside: {upside:.2f}%")
    
    if upside > 0.5:   # Lower threshold for testing
        today_preds.append({
            'Date': date.today().isoformat(),
            'Symbol': symbol,
            'Current_CMP': current,
            'Predicted_EOD': predicted,
            'Upside_%': round(upside, 2),
            'Actual_NextDay': None,
            'Hit': None
        })
        print(f"   ✅ Added to predictions")

df_today = pd.DataFrame(today_preds)

if not df_today.empty:
    df_today = df_today.nlargest(10, 'Upside_%')
    print(f"\n🎯 Top {len(df_today)} predictions selected.")
else:
    print("\n⚠️ No stocks met the upside criteria.")

# Append to history
history = pd.concat([history, df_today], ignore_index=True)
history.to_csv(csv_path, index=False)

print(f"\n✅ Daily prediction completed! Generated {len(df_today)} predictions.")
print(f"Total records in CSV: {len(history)}")

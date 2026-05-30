import pandas as pd

def add_technical_indicators(df):
    df = df.copy()
    
    # Very basic and safe indicators only
    df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
    df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
    
    # Simple Return
    df['Return'] = df['Close'].pct_change()
    
    # Drop NaN
    df = df.dropna().reset_index(drop=True)
    
    return df

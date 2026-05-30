import pandas as pd

def add_technical_indicators(df):
    df = df.copy()
    df['Return'] = df['Close'].pct_change()
    df = df.dropna().reset_index(drop=True)
    return df

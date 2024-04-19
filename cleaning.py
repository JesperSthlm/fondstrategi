import pandas as pd

def cleaning(df):

    df.set_index('Date', inplace=True)

    df['next_mth'] = df.groupby('fond_id')['Price'].shift(-1)
    df['roi'] = df['next_mth'] / df['Price']

    # Change from previous month
    df['monthly_change'] = ((df['Price'] - df.groupby('fond_id')['Price'].shift(1)) / df.groupby('fond_id')['Price'].shift(1)) * 100

    # Return on investment if purchasing said fund now and holding 1 month
    df['roi'] = df.groupby('fond_id')['monthly_change'].shift(-1)

    # Current index contains duplicates
    df.reset_index(inplace=True)

    # Calculate rolling averages
    df.loc[:, 'SMA_1'] = df.groupby('fond_id')['monthly_change'].rolling(window=1).mean().reset_index(level=0, drop=True)
    df.loc[:, 'SMA_2'] = df.groupby('fond_id')['monthly_change'].rolling(window=2).mean().reset_index(level=0, drop=True)
    df.loc[:, 'SMA_3'] = df.groupby('fond_id')['monthly_change'].rolling(window=3).mean().reset_index(level=0, drop=True)
    df.loc[:, 'SMA_4'] = df.groupby('fond_id')['monthly_change'].rolling(window=4).mean().reset_index(level=0, drop=True)
    df.loc[:, 'SMA_5'] = df.groupby('fond_id')['monthly_change'].rolling(window=5).mean().reset_index(level=0, drop=True)
    df.loc[:, 'SMA_6'] = df.groupby('fond_id')['monthly_change'].rolling(window=6).mean().reset_index(level=0, drop=True)

    return df
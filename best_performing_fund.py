import pandas as pd

# Initialize an empty list to store (Date, fond_id) tuples
highest_sma6_fond_ids_with_dates = []

def best_performing_fund( df):
    dates = df['Date'].unique()
    for date in dates:
        # Get the index of the row with the highest SMA_6 for the current date
        index_of_max_sma6 = df[df['Date'] == date]['SMA_6'].nlargest(1).index
        
        # Use the index to get the corresponding fond_id
        fond_id = df.loc[index_of_max_sma6, 'fond_id'].values[0]
        
        # Append the (Date, fond_id) tuple to the list
        highest_sma6_fond_ids_with_dates.append((date, fond_id))

    return highest_sma6_fond_ids_with_dates
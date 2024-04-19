import pandas as pd 

def average_roi(df):

    df = df.pivot(index='Date', columns=['fond_id']).drop(['Price','monthly_change'],axis=1)
    df.fillna(0, inplace=True)
    df.columns = ['_'.join(map(str, col)) for col in df.columns.values]

    # Initialize an empty DataFrame to store average ROI values
    average_roi_df = pd.DataFrame(index=df.index)

    # Iterate over each SMA type
    for sma_type in ['SMA_1','SMA_2','SMA_3','SMA_4','SMA_5','SMA_6']:
        # Find columns for this SMA type
        sma_columns = [col for col in df.columns if col.startswith(sma_type)]

        # For each row, find the top n SMAs and calculate average ROI
        for index, row in df.iterrows():
            # Get the top n SMA columns for this row
            top_sma_columns = row[sma_columns].nlargest(1).index

            # Extract the corresponding fond_ids from the SMA columns
            fond_ids = [col.split('_')[-1] for col in top_sma_columns]

            # Find corresponding ROI columns
            roi_columns = [f'roi_{fond_id}' for fond_id in fond_ids]

            # Calculate average ROI for these columns
            average_roi = row[roi_columns].mean()

            # Store the average ROI in a new DataFrame
            average_roi_df.loc[index, sma_type] = average_roi

    return average_roi_df
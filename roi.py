import pandas as pd

def roi(initial_investment, average_roi_df):
    # Iterate through each SMA column and calculate cumulative growth
    for column in average_roi_df.columns:
        # Convert percentages to growth factors (assuming your percentages are already in decimal form)
        growth_factors = 1 + average_roi_df[column] / 100

        # Calculate the cumulative product
        cumulative_growth = growth_factors.cumprod() * initial_investment

        # Create a new column for this cumulative growth
        average_roi_df[f'cumulative_growth_{column}'] = cumulative_growth - 1000

    calculation = average_roi_df[
                                ['cumulative_growth_SMA_1',
                                    'cumulative_growth_SMA_2',
                                    'cumulative_growth_SMA_3',
                                    'cumulative_growth_SMA_4',
                                    'cumulative_growth_SMA_5',
                                    'cumulative_growth_SMA_6']
                                    ]
    return calculation
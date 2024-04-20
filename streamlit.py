import streamlit as st
import pandas as pd
from average_roi import average_roi
from best_performing_fund import best_performing_fund
from cleaning import cleaning
from fond_data import fond_data
from plots import plots
from roi import roi

# Set Streamlit configuration to suppress pyplot global use deprecation warning
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Algot Raiders fonder")
    st.markdown(
    """
    This tool collects monthly data from Avanza's most popular funds based on number of owners and runs a 
    correlation + momentum algorithm to find the fund predicted to yield the highest return on investment for the next month.

    Historical performance is based on re-balancing at the end of each month. 
    """
    )

    # Define the initial investment and the orderbook IDs
    initial_investment = 50000
    orderbook_ids = [325406,1887,1933,512559,788394,377804,2111,788393,363,693994,2801,852914,736,94867,350,1959,1996,302887,589935,114006,2016,788397,2128,2026,708773,953015,96927,375216, 70789,1089362,132510,2007,728,464,471796,1509086,1877,1158131,715,155953,648075,510,157699,281,367456,404075,574]
    
    # Fetch and process data on button click
    if st.button('Run algorithm'):
        # Initialize an empty DataFrame to store all data points
        all_data_points = pd.DataFrame()

        # Fetch and clean data
        df = fond_data(all_data_points, orderbook_ids)
        df = cleaning(df)

        # Calculate best performer and ROI
        performer = best_performing_fund(df)
        average_roi_df = average_roi(df)
        calculation = roi(initial_investment, average_roi_df)

        # Plot results
        fig = plots(calculation)
        st.pyplot(fig)

        # Show best performers table
        performer_df = pd.DataFrame(performer).sort_values(by=0).tail(6).rename(columns={1: 'Fond ID to purchase'})
        # Convert the '0' column to datetime
        performer_df[0] = pd.to_datetime(performer_df[0])

        # Format the date to year-month and add one month
        performer_df[0] = performer_df[0] + pd.DateOffset(months=1)
        performer_df[0] = performer_df[0].dt.strftime('%Y-%m')

        performer_df = performer_df.rename(columns={0:'Prediction month'})
        st.table(performer_df)

        # Display the image below the table
        image_url = 'https://i.imgur.com/WvhYQHu.png'
        st.image(image_url, caption='Fund ID location', use_column_width=True)

# Ensure the file is run directly and not imported
if __name__ == "__main__":
    main()

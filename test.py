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
        st.table(performer_df)

# Ensure the file is run directly and not imported
if __name__ == "__main__":
    main()

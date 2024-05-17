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
    
    # Your set of tuples
    fond_data_set = {
        (325406, "Spiltan Aktiefond Investmentbolag"),
        (1887, "AMF Aktiefond Global"),
        (1933, "Swedbank Robur Ny Teknik A"),
        (512559, "Handelsbanken Hållbar Energi A1 SEK"),
        (788394, "Avanza Auto 6"),
        (377804, "Avanza 75"),
        (2111, "AMF Räntefond Lång"),
        (788393, "Avanza Auto 5"),
        (363, "Swedbank Robur Technology A"),
        (693994, "Spiltan Globalfond Investmentbolag"),
        (2801, "AMF Aktiefond Småbolag"),
        (852914, "Kavaljer Investmentbolagsfond A"),
        (736, "AMF Aktiefond Europa"),
        (94867, "Spiltan Räntefond Sverige"),
        (350, "Länsförsäkringar Fastighetsfond A"),
        (1959, "Handelsbanken Sverige (A1 SEK)"),
        (1996, "Spiltan Småbolagsfond"),
        (302887, "Nordea 1 - Emerging Stars Equity BP SEK"),
        (589935, "Enter Småbolagsfond A"),
        (114006, "JPM Emerging Markets Equity A (acc) USD"),
        (2016, "Spiltan Aktiefond Stabil"),
        (788397, "Avanza Auto 3"),
        (2128, "Storebrand Obligation A SEK"),
        (2026, "Swedbank Robur Räntefond Kort A"),
        (708773, "Storebrand Global Multifactor A"),
        (953015, "Proethos Fond"),
        (96927, "AMF Aktiefond Nordamerika"),
        (375216, "Storebrand Global Solutions A SEK"),
        (70789, "Schroder ISF Glb Em Mkt Opps A Acc USD"),
        (1089362, "Captor Iris Bond A"),
        (132510, "Spiltan Aktiefond Småland"),
        (2007, "SEB Sverigefond Småbolag C/R"),
        (728, "SEB Europe Equity Fund C EUR"),
        (464, "Handelsbanken Hälsovård Tema (A1 SEK)"),
        (471796, "Spiltan Högräntefond"),
        (1509086, "DNB Teknologi S"),
        (1877, "Swedbank Robur Globalfond A"),
        (1158131, "Thematica - Future Mobility Retl SEK Acc"),
        (715, "CT (Lux) Sust Opps Eurp Eq A Inc EUR"),
        (155953, "Lannebo Sverige Plus"),
        (648075, "Simplicity Sverige"),
        (510, "Öhman Global A"),
        (157699, "Didner & Gerge Småbolag"),
        (281, "AMF Balansfond"),
        (367456, "East Capital Global EM Sustainable A SEK"),
        (404075, "Tundra Sustainable Frontier Fund A SEK"),
        (574, "Swedbank Robur Europafond A")
    }

    # Create the mapping dictionary
    fond_dict = dict(fond_data_set)

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
        performer_df = pd.DataFrame(performer).sort_values(by=0).tail(6).rename(columns={1: 'Fund ID to purchase'})
        # Convert the '0' column to datetime
        performer_df[0] = pd.to_datetime(performer_df[0])

        # Format the date to year-month and add one month
        performer_df[0] = performer_df[0] + pd.DateOffset(months=1)
        performer_df[0] = performer_df[0].dt.strftime('%Y-%m')

        performer_df = performer_df.rename(columns={0:'Prediction month'})

        performer_df['Name of fund'] = performer_df['Fund ID to purchase'].map(fond_dict)

        st.table(performer_df)

        # Display the image below the table
        image_url = 'https://i.imgur.com/WvhYQHu.png'
        st.image(image_url, caption='Fund ID location', use_column_width=True)

# Ensure the file is run directly and not imported
if __name__ == "__main__":
    main()

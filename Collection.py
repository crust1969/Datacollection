import os
import pandas as pd
import streamlit as st

# Streamlit app
st.title('CSV Data Loader and Viewer')

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the data
    data_frame = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.header('Loaded Data')
    st.dataframe(data_frame)
else:
    st.info("Please upload a CSV file.")

if __name__ == "__main__":
    st.set_page_config(page_title='CSV Data Loader', layout='wide')

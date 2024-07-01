import os
import pandas as pd
import streamlit as st

# Specify the directory and file name
directory = '/Users/carstenrust/Documents'
file_name = 'data.csv'
file_path = os.path.join(directory, file_name)

# Function to load data from CSV file
def load_data(file_path):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        st.error(f"File {file_path} does not exist.")
        return None

# Streamlit app
st.title('Data Loader and Viewer')

# Load the data
data_frame = load_data(file_path)

# Display the DataFrame
if data_frame is not None:
    st.header('Loaded Data')
    st.dataframe(data_frame)

if __name__ == "__main__":
    st.set_page_config(page_title='Data Loader', layout='wide')


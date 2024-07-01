import streamlit as st
import pandas as pd

# File path to the CSV file
file_path = '/Users/carstenrust/Documents/data.csv'

# Function to load data from CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to write data to CSV file
def write_data(file_path, df):
    df.to_csv(file_path, index=False)

# Load existing data
df = load_data(file_path)

# Streamlit app
st.title('CSV Data Manager')

# Display existing data
st.header('Existing Data')
st.dataframe(df)

# Form to add new data
st.header('Add New Data')
with st.form('data_form'):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input('Name')
        age = st.number_input('Age', min_value=0, max_value=120, step=1)
    with col2:
        gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
        country = st.text_input('Country')
    
    submitted = st.form_submit_button('Add Data')
    
    if submitted:
        # Append new data to the DataFrame
        new_data = {'Name': name, 'Age': age, 'Gender': gender, 'Country': country}
        df = df.append(new_data, ignore_index=True)
        
        # Write the updated DataFrame back to the CSV file
        write_data(file_path, df)
        
        st.success('Data added successfully!')
        st.dataframe(df)  # Display updated data

if __name__ == "__main__":
    st.set_page_config(page_title='CSV Data Manager', layout='wide')
    main()

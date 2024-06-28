import streamlit as st
from openpyxl import Workbook

st.title('Excel Data Entry App')

# Get user input
user_input = st.text_input('Enter data:')

if st.button('Save to Excel'):
    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Write user input to Excel
    ws.append([user_input])

    # Specify the full path to save the Excel file in the Documents directory
    file_path = "/Users/carstenrust/Documents/data.xlsx"

    # Save the Excel file to the specified directory
    wb.save(file_path)
    st.success(f'Data saved to {file_path}')

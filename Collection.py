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

    # Save the Excel file
    wb.save('/Users/carstenrust/Documents/data.xlsx')
    st.success('Data saved to data.xlsx')

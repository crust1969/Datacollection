import os
import streamlit as st
from openpyxl import Workbook

# Define the file path where you want to save the Excel file
file_path = "/Users/carstenrust/Documents/data.xlsx"

# Create the directory if it does not exist
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Create a new Excel workbook
wb = Workbook()

# Create a sample worksheet
ws = wb.active
ws.title = "Data"
ws["A1"] = "Hello"
ws["B1"] = "World"

try:
    # Attempt to save the workbook to the specified file path
    wb.save(file_path)
    st.success(f"Excel file saved successfully at: {file_path}")
except Exception as e:
    st.error(f"An error occurred while saving the Excel file: {e}")



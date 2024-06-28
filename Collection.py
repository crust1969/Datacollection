import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import os
import tempfile

# Function to write data to the Excel file
def write_to_excel(file_path, data):
    try:
        # Load the existing Excel file
        book = load_workbook(file_path)
        writer = pd.ExcelWriter(file_path, engine='openpyxl')
        writer.book = book

        # Convert data to a DataFrame
        df = pd.DataFrame(data, index=[0])

        # Write data to the sheet
        df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)

        # Save the Excel file
        writer.save()
        writer.close()  # Close the writer after saving
    except Exception as e:
        st.error(f"Error occurred while writing to Excel: {e}")

# Main function of the Streamlit app
def main():
    st.title("Write Data to Uploaded Excel File")

    # File upload for the Excel file
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file:
        # Save the uploaded file to a temporary location
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())
        file_path = temp_file.name

        # Display the uploaded file
        st.write("Uploaded file:", uploaded_file.name)

        # Data input for the Excel file
        with st.form("data_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name")
                age = st.number_input("Age", min_value=0, max_value=120, step=1)
            with col2:
                gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                country = st.text_input("Country")

            submitted = st.form_submit_button("Save")

        if submitted:
            # Data as a dictionary
            data = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Country": country
            }

            # Write data to the Excel file (passing the file path)
            write_to_excel(file_path, data)
            st.success("Data saved successfully!")

if __name__ == "__main__":
    main()

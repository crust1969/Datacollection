import streamlit as st
import pandas as pd
import os

st.title("Excel File Editor")

# Function to save DataFrame to Excel file
def save_dataframe_to_excel(df, file_path):
    df.to_excel(file_path, index=False)
    st.success(f"Data successfully saved to {file_path}")

# Sidebar for file upload
st.sidebar.header("Load and Edit Excel File")
uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Load the Excel file into a DataFrame
    if 'df' not in st.session_state:
        st.session_state.df = pd.read_excel(uploaded_file)
    st.write("Current content of the file:")
    st.write(st.session_state.df)
    
    # Sidebar for adding new entries
    st.sidebar.header("Add New Entries")
    
    with st.sidebar.form(key='entry_form'):
        new_entries = []
        num_entries = st.number_input("Number of new entries", min_value=1, step=1)
        
        for i in range(num_entries):
            new_entry = {}
            for col in st.session_state.df.columns:
                new_entry[col] = st.text_input(f"{col} (Entry {i+1})", key=f"{col}_{i}")
            new_entries.append(new_entry)
        
        add_entries_button = st.form_submit_button(label="Add Entries")
    
    if add_entries_button:
        all_filled = all(all(entry.values()) for entry in new_entries)
        if all_filled:
            new_rows = pd.DataFrame(new_entries)
            st.session_state.df = pd.concat([st.session_state.df, new_rows], ignore_index=True)
            st.write("Updated content of the file:")
            st.write(st.session_state.df)
        else:
            st.sidebar.error("Please fill in all fields for each entry before adding.")
    
    # Save the updated DataFrame back to the original Excel file
    if st.sidebar.button("Save to Original Excel"):
        save_path = os.path.join(os.getcwd(), uploaded_file.name)
        save_dataframe_to_excel(st.session_state.df, save_path)

    # Save the updated DataFrame to a new file specified by the user
    st.sidebar.header("Save Updated File to New Path")
    save_path = st.sidebar.text_input("Enter path to save updated file", value=os.path.join(os.getcwd(), "updated_" + uploaded_file.name))
    
    if st.sidebar.button("Save Updated File"):
        save_dataframe_to_excel(st.session_state.df, save_path)
else:
    st.sidebar.warning("Please upload an Excel file to proceed.")

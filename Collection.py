import streamlit as st
import os
import pandas as pd

st.title("Lokales Verzeichnis durchsuchen")

# Pfad zum lokalen Verzeichnis
directory_path = st.text_input("Geben Sie den Pfad zum Verzeichnis ein:", "/Users/carstenrust/Documents/")

if os.path.exists(directory_path):
    files = os.listdir(directory_path)
    st.write(f"Dateien im Verzeichnis '{directory_path}':")
    st.write(files)
    
    selected_file = st.selectbox("Wählen Sie eine Datei aus:", files)
    
    if selected_file:
        file_path = os.path.join(directory_path, selected_file)
        if selected_file.endswith('.csv'):
            df = pd.read_csv(file_path)
            st.write(df)
        else:
            st.write(f"Der Dateityp von '{selected_file}' wird nicht unterstützt.")
else:
    st.error("Das angegebene Verzeichnis existiert nicht.")

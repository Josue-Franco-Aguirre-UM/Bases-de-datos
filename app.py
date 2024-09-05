import streamlit as st
import pandas as pd

def _extract_employees_from_excel(excel_file):
        """Extracts employee information from the provided Excel file."""
        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            st.write(f"Error reading the Excel file: {e}")
            return []

        df = df.rename(columns={
            'codigo_Empleado': 'code',
            'Empleado': 'employee',
            'Email': 'email',
        })

        df['code'] = df['code'].astype(str)
        
        st.write(df)

def _extract_employees_details_from_excel(excel_file):
        """Extracts employee information from the provided Excel file."""
        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            st.write(f"Error reading the Excel file: {e}")
            return []

        df = df.rename(columns={
            'codigo_Empleado': 'code',
            'Area': 'area',
            'Horario': 'schedule',
        })

        df['code'] = df['code'].astype(str)
        
        st.write(df)


st.title("Upload employee information Excel files")

uploaded_file_employees = st.file_uploader("Employee list Excel file", type=["xls", "xlsx"])
uploaded_file_details = st.file_uploader("Employee details list Excel file", type=["xls", "xlsx"])

if uploaded_file_employees is not None:
    st.write("Employee list file was uploaded successfully.")
    _extract_employees_from_excel(uploaded_file_employees)

if uploaded_file_details is not None:
    st.write("Employee details file was uploaded successfully.")
    _extract_employees_details_from_excel(uploaded_file_details)
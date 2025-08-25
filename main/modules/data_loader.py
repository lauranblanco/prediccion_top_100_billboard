import pandas as pd
import streamlit as st
from utils.drive_connector import get_excel_data

@st.cache_data(ttl=300)  # Cache por 5 minutos
def load_data(file_name):
    """Carga datos desde Google Drive con cache"""
    try:
        raw_data = get_excel_data(file_name)
        df = pd.DataFrame(raw_data)
        
        # Procesamiento básico
        if 'Fecha' in df.columns:
            df['Fecha'] = pd.to_datetime(df['Fecha'])
            df = df.sort_values('Fecha')
            
        return df
    except Exception as e:
        st.error(f"Error cargando datos: {e}")
        return pd.DataFrame()
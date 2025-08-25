import streamlit as st
import pandas as pd
from modules.data_loader import load_data
from modules.visualizations import plot_time_series, plot_bar_chart

def show():
    st.title("📊 Dashboard Principal")
    
    # Cargar datos
    df = pd.DataFrame() #load_data("Mi-Archivo-Excel")
    
    if not df.empty:
        # Métricas rápidas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Ventas", f"${df['Ventas'].sum():,.0f}")
        with col2:
            st.metric("Promedio Diario", f"${df['Ventas'].mean():,.0f}")
        with col3:
            st.metric("Registros", len(df))
        
        # Gráficos
        plot_time_series(df, 'Fecha', 'Ventas', 'Evolución de Ventas')
        plot_bar_chart(df, 'Producto', 'Ventas', 'Ventas por Producto')
        
        # Dataframe interactivo
        st.subheader("Datos Crudos")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No se pudieron cargar los datos")
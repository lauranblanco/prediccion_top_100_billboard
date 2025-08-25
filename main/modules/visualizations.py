import plotly.express as px
import streamlit as st

def plot_time_series(df, x_col, y_col, title):
    """Crea gráfico de series temporales"""
    fig = px.line(df, x=x_col, y=y_col, title=title)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def plot_bar_chart(df, x_col, y_col, title):
    """Crea gráfico de barras"""
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
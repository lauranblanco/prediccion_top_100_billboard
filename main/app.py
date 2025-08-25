import streamlit as st
#from modules.auth import check_password

# Configuración de la página
st.set_page_config(
    page_title="Mi Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Autenticación (opcional)
# if not check_password():
#     st.stop()  # No continuar si la autenticación falla

# Menú principal en sidebar
with st.sidebar:
    st.title("📊 Mi Dashboard")
    page = st.radio(
        "Navegación",
        ["Dashboard", "Análisis", "Configuración"],
        index=0
    )

# Navegación entre páginas
if page == "Dashboard":
    from pages import Dashboard
    Dashboard.show()
elif page == "Análisis":
    from pages import Analisis
    Analisis.show()
elif page == "Configuración":
    from pages import Configuracion
    Configuracion.show()
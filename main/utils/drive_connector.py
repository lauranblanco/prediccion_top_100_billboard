# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import streamlit as st
# import json

# def connect_to_drive():
#     """Conecta a Google Drive usando service account"""
#     try:
#         scope = ['https://www.googleapis.com/auth/drive']
        
#         # Cargar credenciales desde secrets de Streamlit
#         creds_dict = {
#             "type": "service_account",
#             "project_id": st.secrets["gdrive"]["project_id"],
#             "private_key": st.secrets["gdrive"]["private_key"].replace('\\n', '\n'),
#             "client_email": st.secrets["gdrive"]["client_email"]
#         }
        
#         creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
#         return gspread.authorize(creds)
#     except Exception as e:
#         st.error(f"Error conectando a Google Drive: {e}")
#         return None

# def get_excel_data(file_name):
#     """Obtiene datos de un archivo Excel en Drive"""
#     try:
#         client = connect_to_drive()
#         if client:
#             spreadsheet = client.open(file_name)
#             worksheet = spreadsheet.sheet1
#             return worksheet.get_all_records()
#     except Exception as e:
#         st.error(f"Error accediendo al archivo {file_name}: {e}")
#         return []
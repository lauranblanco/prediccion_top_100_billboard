from dash import Dash, html
from app import app


# Layout principal
app.layout = html.Div([
    html.H1("Hola, Dash"),
    html.H2("Prueba cambios"),
])

# Servidor principal
if __name__ == "__main__":
    app.run_server(debug=True, port=1211)
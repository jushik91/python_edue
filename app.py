from dash import Dash, html, dcc, page_container, page_registry
import dash_bootstrap_components as dbc
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div([
    html.H3("Sidebar"),
    html.Hr(),
    dbc.Nav([ dbc.NavLink(page["name"], href=page["path"], active="exact") for page in page_registry.values()], 
            vertical=True, pills=True)
], style=SIDEBAR_STYLE)

app.layout = dbc.Container([
    dbc.Row([dbc.Col(sidebar, width=2), dbc.Col(page_container, width=10)])
], className='m-2')

import socket

def get_port():
    ports = range(8050, 8550)
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port

if __name__ == '__main__':
    app.run(debug=True, port=get_port())

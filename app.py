import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, dash_table, page_container
import plotly.express as px
import dash_bootstrap_components as dbc
import data as app_data

# Create App
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
	   suppress_callback_exceptions=True, prevent_initial_callbacks=True)
server = app.server

# Load shared components
from assets.footer import _footer
from assets.nav import _nav

# App Layout
app.layout = dbc.Container([
	
	dbc.Row([
        dbc.Col([_nav], width = 2),
        dbc.Col([
            dbc.Row([page_container])
	    ], width = 10),
    ]),
    dbc.Row([
        dbc.Col([], width = 2),
        dbc.Col([
            dbc.Row([_footer])
	    ], width = 10),
    ]),
     dcc.Store(id='browser-memo', data=dict(), storage_type='session')
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
import dash
from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import data

dash.register_page(__name__, name='Team Stats', title='IceHockey_Analysis | Team Stats')

layout = dbc.Container([
    dbc.Row([
            dbc.Col([dcc.Dropdown(options=data.seasons ,placeholder='Season', clearable=False, searchable=True, persistence=True, persistence_type='memory', id='p-fin')], width=1),
        ]), 
])
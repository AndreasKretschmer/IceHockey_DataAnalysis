import dash
from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import data.data

dash.register_page(__name__, path='/teams', name='Team Stats', title='IceHockey_Analysis | Team Stats')

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([html.H3(['Team Statistics'])], width=12, className='row-titles')
    ]),

    # data input    
    dbc.Row([
            dbc.Col([dcc.Dropdown(options=data.data.seasons ,placeholder='Season', clearable=False, searchable=True, persistence=True, persistence_type='memory', id='Season')], width=1),
            dbc.Col([dcc.Dropdown(options=data.data.teams ,placeholder='Team', clearable=False, searchable=True, persistence=True, persistence_type='memory', id='Team')], width=1),
        ]), 
])
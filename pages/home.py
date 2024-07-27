import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Home', title='IceHockey_Analysis | Home')

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([
            html.H3(['Hey!']),
            html.P([html.B(['App Overview'])], className='par')
        ], width=12, className='row-titles')
    ]),
    # Guidelines
    dbc.Row([
        dbc.Col([], width = 2),
        dbc.Col([
            html.P([html.B('About'),html.Br(),
                    'Enter a Description of the Project here'], className='guide'),
        ], width = 8),
        dbc.Col([], width = 2)
    ])
])
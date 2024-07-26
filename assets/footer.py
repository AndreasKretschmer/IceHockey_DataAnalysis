from dash import html
import dash_bootstrap_components as dbc

_footer = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([html.Hr([], className = 'hr-footer')], width = 12)
        ]),
        dbc.Row([
	        dbc.Col([], width = 1),
            dbc.Col(['Created with Plotly Dash'], width = 3),
            dbc.Col([], width =6),
	        dbc.Col([
                html.Ul([
                    html.Li([
                        html.A([ html.I(className="github link-me")], href="https://github.com/AndreasKretschmer/IceHockey_DataAnalysis"),
                        html.A([ html.I(className="linkedin link-me")], href="https://www.linkedin.com/in/andreas-kretschmer-61ba76190/"),
                    ])
                ], className='links-me')
            ], width = 2)
        ])
    ], fluid=True)
], className = 'footer')
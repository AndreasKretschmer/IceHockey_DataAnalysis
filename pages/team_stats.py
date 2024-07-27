import dash
from dash import html, callback, Input, Output, dcc, dash_table
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
            dbc.Col([dcc.Dropdown(options=data.data.seasons['season'] ,placeholder='Season', clearable=False, searchable=True, persistence=True, persistence_type='memory', id='season-dd')], width=2),
            # dbc.Col([dcc.Dropdown(options=data.data.teams ,placeholder='Team', clearable=True, searchable=True, persistence=True, persistence_type='memory', id='team-dd')], width=1),
        ]), 

    # raw data table
    dbc.Row([
        dbc.Col([], width = 2),
        dbc.Col([
            dcc.Loading(id='p1_1-loading', type='circle', children=dash_table.DataTable(data.data.teams.to_dict('records'),[{"name": i, "id": i} for i in data.data.teams.columns], id='fig-pg1'), className='team-stats-table')
        ], width = 8),
        dbc.Col([], width = 2)
    ], className='row-content')        
])

### PAGE CALLBACKS ###############################################################################################################

# Update fig
@callback(
    Output(component_id='fig-pg1', component_property='figure'),
    [
        Input(component_id='season-dd', component_property='value'),
        # Input(component_id='team-dd', component_property='value'),
    ]
)
def plot_data(season_value):
    pass
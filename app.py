import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px

data = pd.read_csv("data\game.csv").query("home_team_id==16").assign(Date=lambda data: pd.to_datetime(data["date_time_GMT"], format="%Y-%m-%dT%H:%M:%SZ")).sort_values(by="Date")
data['season'] = data['season'].astype(str)
season_outcomes = data.groupby(["season", "outcome"]).size().unstack(fill_value=0).reset_index().melt(id_vars='season', var_name='outcome', value_name='count')
app = Dash(__name__)

fig = px.bar(season_outcomes, x='season', y='count', color='outcome', barmode='group',
             labels={'season': 'Season', 'count': 'Count', 'outcome': 'Outcome'},
             title='Outcome Counts per Season')

app.layout = html.Div(
        children=[
            html.H1(children="Ice Hockey Data Analysis"),
            html.P(
                children=(
                    "Analyzing Data of NHL Seasons from ---- to ----"
                ),
            ),
            dash_table.DataTable(data.to_dict('records'), [{"name": i, "id": i} for i in data.columns]),
            dcc.Graph(
                id='Season Outcomes',
                figure=fig,
            ),
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)
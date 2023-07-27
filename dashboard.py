import plotly.express as px
import dash
import pandas as pd
import numpy as np
from dash import dcc, html, Output
from dash.dependencies import Input


app = dash.Dash('spark-app')

app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='graph-update',
        interval=1 * 1000,
        n_intervals=0,
    )
])


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    return px.line(
        pd.read_csv('data.csv').groupby('laps')['averageSpeed'].mean().reset_index(),
        x='laps',
        y='averageSpeed',
        labels={'vitesse': 'Moyenne des vitesses'},
    )


app.run_server(port=8080, debug=True)

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.nav import NavBar


import plotly.express as px
import pandas as pd
from app import app
import dash_bootstrap_components as dbc


from app import app

# mettre le code ici ( layout + callbacks)

active = "page2"
nav = NavBar(active)

jeunes_morts = pd.read_csv("data/jeunes_morts_cont.csv")
pays_possibles = jeunes_morts.Country.unique()

layout = html.Div([
    html.Div(className="NavBar",children=[nav]),
    html.Div([
        html.H1('Page 2',style={"color":"white"}),
        dbc.Row([
                dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': str(i), 'value': str(i)} for i in pays_possibles],
                value='France'
                ),
        ],
        style={"width":"95%","height":"100%","display":"inline-block","margin-left":"50px","margin-right":"50px"}
        ),
        dbc.Row([
                dcc.Graph(id='indicator-graphic'),

        ],
        style={"width":"100%","height":"100%","display":"inline-block"}
        ),
        ],style={'width': '100%','height': '100%',"background":"#131414","margin-top":"70px"}),
])



@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value')])
def update_graph(xaxis_column_name):
    jeunes_morts = pd.read_csv("data/jeunes_morts_cont.csv")
    df = jeunes_morts[jeunes_morts.Country == xaxis_column_name]
    df = df[['Year' , 'Value']].groupby('Year').max()
    fig = px.line(df,template="plotly_dark",labels={"variable":"Nbr de morts"})
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(title=xaxis_column_name)


    return fig

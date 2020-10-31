import base64
import datetime
import io

from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from apps.nav import NavBar

from app import app
import pandas as pd

active = "page3"
nav = NavBar(active)


layout = html.Div([
    html.Div(className="NavBar",children=[nav]),
    dcc.Dropdown(
        id='upload-data',
        options=[{"label":"Data sur l'alcool","value":"DataAlcool"},
                 {"label":"Data sur les accidents","value":"DataAccident"},
                 {"label":"Data sur la législation","value":"DataTolerance"},
                ],
        value="DataAlcool"
    ),
    html.Div(id='output-data-upload',style={"width":"90%"}),
], style={'width': '100%','height': '100%',"background":"#212121","margin-top":"70px"})

# Création d'une fonction qui affiche sous forme d'un tableau les csv demandés,prend comme parametre une string indiquant le chemin d'accès au fichier
def parse_contents(filename):

    df = pd.read_csv(filename)
    print(df),
    return html.Div([
        html.H5(filename,style={"color":"white"}),


        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'value')])
def update_output(names):
    if names == "DataAlcool":
        contents = "data/youth_cont.csv"
    elif names == "DataAccident":
        contents = "data/jeunes_morts_cont.csv"
    elif names == "DataTolerance":
        contents = "data/tolerance_compl.csv"
    if contents is not None:
        children = [
            parse_contents(contents)
            ]
        return children

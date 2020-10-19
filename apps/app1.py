import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.nav import NavBar
import plotly.express as px
import pandas as pd
from app import app
import dash_bootstrap_components as dbc

active = "page1"
nav = NavBar(active)

# Figure 1 montrant le pourcentage de jeune qui consomme de l'alcool pour les 15-19 ans
youth = pd.read_csv("data/youth_cont.csv")
fig = px.choropleth(youth , locations='Alpha-3 code', color='15-19 years old, current drinkers both sexes (%)',
                           color_continuous_scale="Peach",
                           range_color=(0, 100),
                           scope="world",
                           labels={'15-19 years old, current drinkers both sexes (%)':"consommation d'alcool<br> pour les 15-19 ans"},
                           template="plotly_dark",
                          )


fig.update_layout(title_text = "% de jeune consommant de l'alcool"),
fig.update_layout(margin={"r":0,"t":30,"l":0,"b":30}),

jeunes_morts = pd.read_csv("data/jeunes_morts_cont.csv")
pays_possibles = jeunes_morts.Country.unique()
continents_possibles = youth.Continent.unique()

tab_total = dbc.Card(
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='map',
                    figure=fig
                ),
            ]),
        ]),
        dbc.Row([
            dcc.Dropdown(
                id = "pays_select",
                options = [{'label': str(i), 'value': str(i)} for i in continents_possibles if str(i)!="nan" and str(i)!="OC"],
                value="EU"
            ),
        ],style={"width":"95%","height":"100%","display":"inline-block","margin-left":"50px","margin-right":"50px"}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='map2',
                ),
            ]),
        ]),

    ]), className ="mt-3", style = {'width': '100%','height': '100%',"background":"#131414"},
)

tab_homme = ""

tab_femme = ""

# Layout de la page permettant d'afficher les differents éléments
layout = html.Div([
    html.Div(className="NavBar",children=[nav]),

    html.Div([
        html.H1(["Visualisation sur la consommation d'alcool chez les jeunes"],style={"color":"white","text-align":"center",}),
        dbc.Tabs([
            dbc.Tab(tab_total,label="Total"),
            dbc.Tab(tab_homme,label="Homme"),
            dbc.Tab(tab_femme, label="Femme"),
        ])

    ], style={'width': '100%','height': '100%',"background":"#131414","margin-top":"70px"})
]),


@app.callback(
    Output("map2","figure"),
    [Input("pays_select","value")]
)
def upgrade_map(pays_select):
    pays = "europe"
    name = "Europe"
    if pays_select == "SA":
        pays = "south america"
        name = "Amerique du sud"
    elif pays_select == "AS":
        pays = "asia"
        name = "Asie"
    elif pays_select == "AF":
        pays = "africa"
        name = "Afrique"
    else :
        pays = "europe"

    fig2 = px.choropleth(youth ,
                               locations='Alpha-3 code',
                               color='15-19 years old, current drinkers both sexes (%)',
                               color_continuous_scale="Viridis",
                               range_color=(0, 100),
                               scope=pays,
                               labels={'15-19 years old, current drinkers both sexes (%)':"consommation d'alcool<br> pour les 15-19 ans"},
                               template="plotly_dark",
                              )
    fig2.update_layout(title_text = "% de jeune consommant de l'alcool en "+ name),
    fig2.update_layout(margin={"r":0,"t":30,"l":0,"b":0})

    return fig2

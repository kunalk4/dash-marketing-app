import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

layout = html.Div([html.P("This application uses the SimilarWeb API to process data for website traffic analysis. \
                            Simply enter a website into the search box below and the three KPI's shown in the navigation bar will be generated!", 
                            style={'fontSize': 28}),
                  html.Div(
                            [
                                dbc.Input(id="input", placeholder="Enter website", type="text"),
                                html.Br(),
                                html.P(id="output"),
                            ]
                            )
                            ]
                )
                
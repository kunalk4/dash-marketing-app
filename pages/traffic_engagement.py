### Import Packages ###
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div(
    children=[
        html.H1(
            children='Traffic Distribution',
        ),
        dcc.Dropdown(
            id='page-1-dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA',
        ),
        html.Div(
            id='page-1-content',
        ),
        html.Br(),
        dcc.Link(
            children='Go to Age Distribution',
            href='/age-distribution',
        ),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ]
)
@app.callback(
    Output(
        component_id='page-1-content',
        component_property='children',
    ),
    [Input(
        component_id='page-1-dropdown',
        component_property='value',
    )]
)
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)
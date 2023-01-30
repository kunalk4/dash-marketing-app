import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div(
    children=[
        html.H1(
            children='Age Distribution',
        ),
        dcc.RadioItems(
            id='page-2-radios',
            options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
            value='Orange',
        ),
        html.Div(
            id='page-2-content',
        ),
        html.Br(),
        dcc.Link(
            children='Go to Traffic Distribution',
            href='/page-1',
        ),
        html.Br(),
        dcc.Link('Go back to home', href='/')
    ]
)
@app.callback(
    Output(
        component_id='page-2-content',
        component_property='children',
    ),
    [Input(
        component_id='page-2-radios',
        component_property='value',
    )]
)
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)
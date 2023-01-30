import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from pages import age_distribution
from pages import home
from pages import marketing_channels
from pages import traffic_engagement
import navbar

from app import app

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(id="page-content", style=CONTENT_STYLE)

# set app main page layout
app.layout = html.Div([dcc.Location(id="url"), navbar.sidebar, content])

### Assemble all layouts ###
app.validation_layout = html.Div(
    children = [
        home.layout,
        traffic_engagement.layout,
        age_distribution.layout,
    ]
)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/page-1":
        return traffic_engagement.layout
    elif pathname == "/page-2":
        return age_distribution.layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
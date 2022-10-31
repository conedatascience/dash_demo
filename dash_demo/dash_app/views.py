"""
Routes and views for the flask application.
"""

from create_app import app
from datetime import datetime
from flask import render_template
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go


cone_colors = {
    "main_lit_blu": "#00A2B2", "main_ylw": "#F1BD51", "main_drk_blu": "#00205C", "lit_gry": "#c9c9c9", 
    "lit_prp": "#7750A9", "lit_grn_ylw": "#B7D866", "drk_gry": "#5C5859", "red": "#DB2B27", 
    "sky_blu": "#63CCFF", "black": "#000000", "lit_ora": "#006620", "drk_grn": "#006620", "pnk": "#F9A3FF", 
    "brt_ylw": "#FFEF0F", "drk_prp": "#292060", "lit_gry_red": "#F7EAE8", "drk_grn_ylw": "#313612", 
    "lit_gry_prp": "#C6BEE9", "lit_grn": "#94C95E", "drk_prp2": "#210B22", "lit_gry_grn": "#D8F0D1", 
    "drk_ora": "#B0813B"
    }

pio.templates["cone_colors"] = go.layout.Template(
    layout = go.Layout(
        colorway = list(cone_colors.values())
    )
)
pio.templates.default = "cone_colors"

data = px.data.iris()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# GRAPH DEMO PAGE

# initiate dash page
graph_demos_page = Dash(
    __name__,
    server = app,
    external_stylesheets = [dbc.themes.BOOTSTRAP],
    url_base_pathname = "/graph_demos/"
    )
from pages.graph_demos import graph_demos_layout
graph_demos_page.layout = graph_demos_layout  # apply layout

# add interactivity functions here
# accept inputs from dropdowns to change x and y axis for scatter plot
@graph_demos_page.callback(
    Output('scatter-plot', 'figure'),
    Input('scatter_x_cols', 'value'),
    Input('scatter_y_cols', 'value')
    )
def update_scatter_plot(x, y):

    fig = px.scatter(
	    data,
	    x = x,
	    y = y,
	    color = "species"
	)

    return fig

# accept input from dropdown and toggle to change histogram feature and color
@graph_demos_page.callback(
    Output('hist-plot', 'figure'),
    Input('hist_cols', 'value'),
    Input('hist_color', 'value')
    )
def update_hist_plot(x, hist_color):
    if hist_color:
        color = "species"
    else:
        color = None

    fig = px.histogram(
	    data,
	    x = x,
	    color = color
	)

    return fig

# render dash page
@app.route('/graph_demos')
def graph_demos():
    """Renders the diagnosis explorer page."""
    return render_template(
        'graph_demos.html',
        title='Demo graphing with plotly',
        year=datetime.now().year,
        message='Demonstrate capabilities of plotly dash with iris dataset.'
    )

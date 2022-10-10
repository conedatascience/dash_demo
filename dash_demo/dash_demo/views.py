"""
Routes and views for the flask application.
"""

from dash_demo import app
from datetime import datetime
from flask import render_template
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

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
from dash_demo.pages.graph_demos import graph_demos_layout
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

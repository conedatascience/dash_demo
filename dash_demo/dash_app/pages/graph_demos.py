from cProfile import label
import pandas as pd
import numpy as np
from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import dash_daq as daq


data = px.data.iris()

x_cols = [
	"sepal_width",
	"petal_width"
	]

y_cols = [
	"sepal_length",
	"petal_length"
	]

hist_cols = [
	"sepal_width",
	"petal_width",
	"sepal_length",
	"petal_length"
	]

body = html.Div(children = [

	html.Br(),

	html.Div([
		html.H1(children = "Demonstrate functionality with Iris dataset")
		]),

	html.Br(),
	
	# scatter plot
	html.Div([
		html.H2(children = "Simple scatter plot with dropdowns"),
		# scatter plot options
		html.Div([
			html.Div([
				html.Label("Choose x column:"),
				dcc.Dropdown(
					x_cols,
					x_cols[0],
					id = "scatter_x_cols",
					clearable = False
					)
				],
			style = {'width': '49%', 'display': 'inline-block'}
			),
			html.Div([
				html.Label("Choose y column:"),
				dcc.Dropdown(
					y_cols,
					y_cols[0],
					id = "scatter_y_cols",
					clearable = False
					)
				],
			style={'width': '49%', 'display': 'inline-block', 'float':'right'}
			)
			]),
		html.Br(),
		# draw scatter plot
		html.Div([
			dcc.Graph(
				id = "scatter-plot"
				)
			])
		]),

	html.Br(),

	# histogram plot
	html.Div([
		html.H2(children = "Simple histogram plot with radio buttons"),
		# histogram options
		html.Div([
			html.Div([
				html.Label("Choose feature:"),
				dcc.RadioItems(
					hist_cols,
					hist_cols[0],
					id = "hist_cols",
					inline = True,
                    inputStyle={'margin-right': '5px', 'margin-left': '5px'}
					)
				],
			style = {'width': '49%', 'display': 'inline-block'}
			),
			html.Div([
				daq.ToggleSwitch(
					label = "Color by species:",
					id = "hist_color",
					value = True
					)
				],
			style={'width': '49%', 'display': 'inline-block', 'float':'right'}
			)
			]),
		html.Br(),
		# draw histogram plot
		html.Div([
			dcc.Graph(
				id = "hist-plot"
				)
			])
		])

	])

from pages.navbar import navigation

def graph_demos_layout():
	layout = html.Div(
		[
			dcc.Location(id="url"),
			navigation,
			body
		],
        style={
            "margin-left": "2rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem"
        }
		)
	return layout

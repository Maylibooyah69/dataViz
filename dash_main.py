# %%

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from preprocess import *
# %%
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='Select  Patient Number'),
    dcc.Dropdown(
            id='patient_id',
            options=[{'label': i, 'value': i} for i in patient_lst],
            value='MR1111569'
        )
    
    
    
    
    ]
    
    
    
    )


# %%
if __name__ == '__main__':
    app.run_server(debug=True)
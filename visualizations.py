import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/creditcard.csv')

app = dash.Dash()

feature_options = []
for feat in df.columns:
    feature_options.append({'label': feat, 'value': feat})

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='histogram'),
        dcc.Dropdown(id='feature-picker', options=feature_options, value='V1')
    ]),

    html.Div([
        dcc.Graph(id='correlation_plot'),
        dcc.Dropdown(id='feature-picker1', options=feature_options, value='V1'),
        dcc.Dropdown(id='feature-picker2', options=feature_options, value='V2')
    ])

])


@app.callback(Output('histogram', 'figure'),
              [Input('feature-picker', 'value')])
def update_figure(selected_feature):

    filtered_df = df[selected_feature]
    data = [
        go.Histogram(
            x=filtered_df,
        )
    ]

    return {
        'data': data,
        'layout': go.Layout(
            hovermode='closest'
        )
    }


@app.callback(Output('correlation_plot', 'figure'),
              [Input('feature-picker1', 'value'),
               Input('feature-picker2', 'value')])
def update_figure(selected_feature1, selected_feature2):

    data = [
        go.Scattergl(
            x=df[selected_feature1],
            y=df[selected_feature2],
            mode = 'markers'
        )
    ]

    return {
        'data': data,
        'layout': go.Layout(
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()

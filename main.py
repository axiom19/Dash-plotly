# Import packages
from dash import Dash, html, dash_table, dcc, callback, Input, Output
import pandas as pd
import ssl
import plotly.express as px

ssl._create_default_https_context = ssl._create_unverified_context

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app and incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    html.H1('My First Webapp Dashboard', style={'textAlign': 'center', 'color': 'gray', 'fontSize': 36}),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='radio-buttons', inline=True),
    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='histo-chart')
        ])
    ])
])


# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart', component_property='figure'),
    Input(component_id='radio-buttons', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', color='continent')
    return fig



# Run the app
if __name__ == '__main__':
    app.run(debug=True)

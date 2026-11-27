from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

server = app.server

app.layout = dbc.Container([
    dbc.Input(
        id='my_text',
        value='Type Text new now'
    ),

    dcc.Markdown(
        id='my_output',
        children=''
    ),
])

@app.callback(
    Output('my_output', 'children'),
    Input('my_text', 'value')
)
def update_text(el_texto):
    return el_texto

if __name__ == '__main__':
    app.run(debug=True)
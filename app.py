from req.NBA import nba
from dash import Dash, dcc, html, Input, Output, State
from tabs.player_information import PlayerInformation
# import plotly.graph_objects as go
# import plotly.express as px

# initialize dash data
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='player-information', children=[
        dcc.Tab(label='Player Information', value='player-information', style=tab_style,
                selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])


@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if (tab == "player-information"):
        playerInformation = PlayerInformation(app)
        return playerInformation.playerInformationContainer


if __name__ == '__main__':
    # development
    # app.run_server(debug=True)
    # production
    app.run_server()

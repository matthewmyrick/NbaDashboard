from dash import html, dcc
from req.NBA import nba

player_information = html.Div([
            html.P("Please Select a Player"),
            dcc.Dropdown(
                id='players-dropdown',
                # type='value',
                options=nba.get_active_players_list_dropdown(),
                clearable=False,
                placeholder='select a player',
                style=dict(width="50%")
            ),
            html.Button('Submit', id='submit-val', n_clicks=0),
            html.Div(id='container-button-basic',
                     children='Enter a value and press submit')
        ], style=dict(padding="1%"))


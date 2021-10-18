from dash import html, dcc, Input, Output, dash_table
from req.NBA import nba


class PlayerInformation:
    playerInformationContainer = html.Div([
        html.P("Please Select a Player"),
        dcc.Dropdown(
            id='players-dropdown',
            value='',
            options=nba.get_active_players_list_dropdown(),
            clearable=False,
            placeholder='select a player',
            style=dict(width="50%")
        ),
        html.Div(id='player-selected', style={"margin-top": "20px"})
    ],

    style=dict(padding="1%"))

    def __init__(self, app):
        @app.callback(
            Output('player-selected', 'children'),
            Input('players-dropdown', 'value')
        )
        def player_information_table(value):
            df = nba.player_regular_season_total_stats(value)
            print(df)
            return dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                ),


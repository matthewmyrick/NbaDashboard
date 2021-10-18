from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
class NBA:
    def get_active_players_list_dropdown(self):
        '''
        This method format the data from the nba-api to the dcc.dropdown in dash
        :return:
        '''
        data = []
        for player in players.get_active_players():
            data.append(
                {
                    'label': player['full_name'],
                    'value': player['id']
                }
            )
        return data

nba = NBA()
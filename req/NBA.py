import pandas
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, PlayerCareerStats
import pandas as pd

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

    def player_regular_season_total_stats(self, player_id):
        '''
          This method format the data from the nba-api to the dcc.dropdown in dash
          :return:
        '''
        data = {}
        player_stats = PlayerCareerStats(player_id=player_id).get_dict()['resultSets']
        for stats in player_stats:
            if stats['name'] == 'SeasonTotalsRegularSeason':
                headers = stats['headers']
                for header in headers:
                    data[header] = []
                for year_stats in stats['rowSet']:
                    for j in range(len(year_stats)):
                        data[headers[j]].append(year_stats[j])
        df = pandas.DataFrame(data)[::-1]
        return df

nba = NBA()
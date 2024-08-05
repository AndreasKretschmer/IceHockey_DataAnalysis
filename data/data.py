import pandas as pd

# import all data into dataframes
games = pd.read_csv('data\\game.csv')
seasons = pd.DataFrame(sorted(games['season'].unique(), reverse=True), columns=['season_id'])
seasons['season'] = seasons['season_id'].astype(str).apply(lambda x: x[:4] + '-' + x[4:])

teams = pd.read_csv('data\\team_info.csv')
players = pd.read_csv('data\\player_info.csv')

game_team_stats = pd.read_csv('data\\game_teams_stats.csv')
game_skater_stats = pd.read_csv('data\\game_skater_stats.csv')
game_goalie_stats = pd.read_csv('data\\game_goalie_stats.csv')

game_goals = pd.read_csv('data\\game_goals.csv')
game_penalties = pd.read_csv('data\\game_penalties.csv')
game_plays = pd.read_csv('data\\game_plays.csv')
game_plays_player = pd.read_csv('data\\game_plays_players.csv')
game_shifts = pd.read_csv('data\\game_shifts.csv')
game_scratches = pd.read_csv('data\\game_scratches.csv')

shots = pd.read_csv('data\\shots.csv')
hits = game_plays.loc[game_plays['event'].isin(['Hit','Shot', 'Blocked Shot', 'Missed Shot'])]

game_officials = pd.read_csv('data\\game_officials.csv')
officials = game_officials['official_name'].unique()

# add season column
game_team_stats = pd.merge(game_team_stats, games[['game_id', 'season', 'type']], on=['game_id'], how='left')
team_stats = game_team_stats.groupby(['season', 'team_id']).sum(numeric_only=True)
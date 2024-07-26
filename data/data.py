import pandas as pd

##import all data into dataframes
games = pd.read_csv("data\\game.csv")
seasons = sorted(games["season"].unique())

teams = pd.read_csv("data\\team_info.csv")
players = pd.read_csv("data\\player_info.csv")

game_team_stats = pd.read_csv("data\\game_teams_stats.csv")
game_skater_stats = pd.read_csv("data\\game_skater_stats.csv")
game_goalie_stats = pd.read_csv("data\\game_goalie_stats.csv")

game_goals = pd.read_csv("data\\game_goals.csv")
game_penalties = pd.read_csv("data\\game_penalties.csv")
game_plays = pd.read_csv("data\\game_plays.csv")
game_plays_player = pd.read_csv("data\\game_plays_players.csv")
game_shifts = pd.read_csv("data\\game_shifts.csv")
game_scratches = pd.read_csv("data\\game_scratches.csv")

shots = game_plays.loc[game_plays["event"].isin(["Goal","Shot", "Blocked Shot", "Missed Shot"])]
hits = game_plays.loc[game_plays["event"].isin(["Hit","Shot", "Blocked Shot", "Missed Shot"])]

game_officials = pd.read_csv("data\\game_officials.csv")
officials = game_officials["official_name"].unique()
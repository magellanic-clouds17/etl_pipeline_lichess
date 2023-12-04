import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Database path
db_path = r'C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed\lichess_13_01.db'

# Create a connection to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL query to find top 10 players by rating increase
query = '''
WITH player_games AS (
    SELECT white_player AS player, game_date, white_elo AS rating 
    FROM games
    UNION ALL
    SELECT black_player, game_date, black_elo 
    FROM games
),
first_game_data AS (
    SELECT player, MIN(game_date) AS first_game_date
    FROM player_games
    GROUP BY player
),
last_game_data AS (
    SELECT player, MAX(game_date) AS last_game_date
    FROM player_games
    GROUP BY player
),
first_game_ratings AS (
    SELECT f.player, f.first_game_date, MIN(pg.rating) AS first_game_rating
    FROM first_game_data f
    JOIN player_games pg ON f.player = pg.player AND f.first_game_date = pg.game_date
    GROUP BY f.player, f.first_game_date
),
last_game_ratings AS (
    SELECT l.player, l.last_game_date, MAX(pg.rating) AS last_game_rating
    FROM last_game_data l
    JOIN player_games pg ON l.player = pg.player AND l.last_game_date = pg.game_date
    GROUP BY l.player, l.last_game_date
),
total_games AS (
    SELECT player, COUNT(*) AS total_games
    FROM player_games
    GROUP BY player
),
combined AS (
    SELECT fgr.player, 
           fgr.first_game_date, 
           fgr.first_game_rating, 
           lgr.last_game_date, 
           lgr.last_game_rating,
           tg.total_games
    FROM first_game_ratings fgr
    JOIN last_game_ratings lgr ON fgr.player = lgr.player
    JOIN total_games tg ON fgr.player = tg.player
)
SELECT player, first_game_date, first_game_rating, last_game_date, last_game_rating, 
       last_game_rating - first_game_rating AS rating_change, total_games
FROM combined
ORDER BY total_games DESC
LIMIT 20;


'''

cursor.execute(query)
top_players = cursor.fetchall()

for player, first_date, first_rating, last_date, last_rating, rating_diff, games in top_players:
    print(f"Player: {player}")
    print(f"Total Games: {games}")
    print(f"First Game: {first_date}, Rating: {first_rating}")
    print(f"Last Game: {last_date}, Rating: {last_rating}")
    print(f"Rating Change: {rating_diff}")
    print('-' * 30)

# close connection
conn.close()


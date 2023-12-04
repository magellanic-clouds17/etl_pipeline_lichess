# import libraries
import pandas as pd
import sqlite3

# connect to database
db_path = r'C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed\lichess_13_01.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

## sql query to find top 10 players by numbers of games played
query = '''
SELECT player, COUNT(*) AS games
FROM (
    SELECT white_player AS player
    FROM games
    UNION ALL
    SELECT black_player AS player
    FROM games
)
GROUP BY player
ORDER BY games DESC
LIMIT 100;
'''
# print player and number of games played
cursor.execute(query)
results = cursor.fetchall()
for player, games in results:
    print(f"{player}: {games} games")
    
# close connection
conn.close()
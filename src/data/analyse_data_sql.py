import sqlite3

# Database path
db_path = r'C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed\lichess_13_01.db'

# Create a connection to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL query to find top 10 players
query = '''
SELECT player, COUNT(*) as num_games
FROM (
    SELECT white_player as player FROM games
    UNION ALL
    SELECT black_player FROM games
) 
GROUP BY player
ORDER BY num_games DESC
LIMIT 10
'''

cursor.execute(query)
top_players = cursor.fetchall()

# Print the top 10 players
for player, games in top_players:
    print(f"{player}: {games} games")

# Close the database connection
conn.close()
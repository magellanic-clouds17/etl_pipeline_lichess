import sqlite3
import chess.pgn
import os

"""
This script reads a PGN (Portable Game Notation) file containing chess game data,
extracts relevant information from each game, and stores it in a SQLite database. 
The data extracted includes player names, their Elo ratings, game results, and dates. 
The script is set up to handle a large volume of games in batches for efficient processing.

Functions:
- extract_utc_date_from_pgn_line: Extracts the UTC date from a line in the PGN file.
- insert_games_batch: Inserts a batch of games into the SQLite database.
"""

# Database path
db_path = r'C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed\lichess_13_01.db'

# Create a connection to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY,
                    white_player TEXT,
                    black_player TEXT,
                    result TEXT,
                    white_elo INT,
                    black_elo INT,
                    game_date DATE
                  )''')
conn.commit()

# Indexing the player names
cursor.execute("CREATE INDEX IF NOT EXISTS idx_white_player ON games(white_player);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_black_player ON games(black_player);")
conn.commit()


# Path to your PGN file
pgn_file_path = r"C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed\lichess_db_standard_rated_2013-01.pgn"

def extract_utc_date_from_pgn_line(line):
    if line.startswith("[UTCDate "):
        return line.split('"')[1]
    return None

def insert_games_batch(games_batch):
    cursor.executemany("INSERT INTO games (white_player, black_player, result, white_elo, black_elo, game_date) VALUES (?, ?, ?, ?, ?, ?)", games_batch)
    conn.commit()

batch_size = 1000
games_batch = []

# Open PGN file
with open(pgn_file_path, 'r', encoding='utf-8') as pgn:
    game = chess.pgn.read_game(pgn)
    while game:
        headers = str(game).split('\n')
        game_date = "Unknown"
        for header in headers:
            if header.startswith("[UTCDate "):
                game_date = extract_utc_date_from_pgn_line(header)
                break
        
        white = game.headers.get('White', 'Unknown')
        black = game.headers.get('Black', 'Unknown')
        result = game.headers.get('Result', '*')
        # Safely convert Elo ratings to integers
        try:
            white_elo = int(game.headers.get('WhiteElo', 0))
        except ValueError:
            white_elo = None

        try:
            black_elo = int(game.headers.get('BlackElo', 0))
        except ValueError:
            black_elo = None

        games_batch.append((white, black, result, white_elo, black_elo, game_date))

        ## Insert batch into database
        if len(games_batch) >= batch_size:
            insert_games_batch(games_batch)
            #break #test run with only 1 batch
            games_batch = []
        
        game = chess.pgn.read_game(pgn)
        
    # Insert any remaining games in the last batch
    if games_batch:
        insert_games_batch(games_batch)     
        
conn.close()

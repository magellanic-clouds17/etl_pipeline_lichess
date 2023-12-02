import chess.pgn
from collections import Counter

def get_top_players(pgn_file_path, top_n=10):
    """
    Analyzes a PGN file of chess games to identify the top players with the most played games.

    Parameters:
    pgn_file_path (str): The file path of the PGN file containing the chess games.
    top_n (int): The number of top players to identify based on the number of games played.

    Returns:
    list: A list of tuples, each containing a player's name and the number of games they played, for the top 'top_n' players.

    The function iterates through the PGN file, extracting player names from each game and counting their occurrences. It then returns a list of the top 'top_n' players sorted by the number of games played.
    """
    # Counter for games played by each player
    player_games_count = Counter()

    # print the collumns of the pgn file
    

    # Open and read the PGN file
    with open(pgn_file_path, 'r', encoding='utf-8') as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break  # No more games in the file

            # Increment count for both white and black players
            white = game.headers.get('White', None)
            black = game.headers.get('Black', None)
            if white:
                player_games_count[white] += 1
            if black:
                player_games_count[black] += 1

    # Find top N players with the most games
    top_players = player_games_count.most_common(top_n)
    return top_players

# Path to your PGN file
pgn_file_path = r"C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed\lichess_db_standard_rated_2013-01.pgn"

# Get top 10 players
top_10_players = get_top_players(pgn_file_path, 10)
for player, games in top_10_players:
    print(f"{player}: {games} games")
    
# print the names of the columns of the pgn file, each column in a sepereate line
with open(pgn_file_path, 'r', encoding='utf-8') as pgn:
    game = chess.pgn.read_game(pgn)
    print(game.headers)
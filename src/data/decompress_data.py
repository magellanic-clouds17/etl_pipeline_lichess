import zstandard as zstd
import os
import chess.pgn

def decompress_zst_file(zst_file_path, output_folder):
    """
    Decompresses a Zstandard (.zst) compressed file and saves the decompressed file in a specified output folder.

    Parameters:
    zst_file_path (str): The file path of the .zst file to be decompressed.
    output_folder (str): The directory where the decompressed file will be saved.

    Returns:
    str: The file path of the decompressed file. If the decompressed file already exists, returns the path of the existing file.

    The function checks if the decompressed file already exists to avoid redundant decompression. If the file doesn't exist, it performs the decompression and saves the output in the specified folder. The filename of the decompressed file is the same as the original file but without the .zst extension.
    """
    # Extract filename without .zst
    filename = os.path.basename(zst_file_path).replace('.zst', '')
    output_file_path = os.path.join(output_folder, filename)

    # Check if the decompressed file already exists
    if os.path.exists(output_file_path):
        print(f"Decompressed file {output_file_path} already exists.")
        return output_file_path

    # Decompress the file
    with open(zst_file_path, 'rb') as compressed:
        with open(output_file_path, 'wb') as decompressed:
            decompressor = zstd.ZstdDecompressor()
            decompressor.copy_stream(compressed, decompressed)
    
    return output_file_path

# Path to the .zst file
zst_file_path = r"C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\raw\lichess_db_standard_rated_2013-01.pgn.zst"

# Output folder
output_folder = r"C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed"

# Decompress the file
decompressed_file = decompress_zst_file(zst_file_path, output_folder)
if decompressed_file:
    print(f"File decompressed to: {decompressed_file}")
    
pgn_file_path = decompressed_file

with open(pgn_file_path, 'r', encoding='utf-8') as pgn:
    flag = True
    counter = 0
    while flag:
        counter += 1
        if counter > 10:
            break
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        
        # Extracting basic info
        event = game.headers.get('Event', 'Unknown')
        white = game.headers.get('White', 'Unknown')
        black = game.headers.get('Black', 'Unknown')
        result = game.headers.get('Result', '*')
        rating_white = game.headers.get('WhiteElo', 'Unknown')
        rating_black = game.headers.get('BlackElo', 'Unknown') 
        moves = game.mainline_moves()
        # Additional processing...

        # Save or print the extracted information
        print(f"{event}: {white} {rating_white} vs {black} {rating_black} - Result: {result}")
        
        # Initialize a new board
        board = game.board()
       
       # Iterate through all the moves in the game
        for move in game.mainline_moves():
            print(board.san(move))
            board.push(move)  # Update the board with the current move
       

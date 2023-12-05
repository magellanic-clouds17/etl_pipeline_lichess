import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import table
import numpy as np

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
ORDER BY rating_change DESC
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

# print table of top 20 players by rating increase and number of games to post in github readme

# Define your data as a list of dictionaries for easier conversion to DataFrame
data_games = [
    {"Player": "F1_ALONSO_FERRARI", "Total Games": 1729, "First Game Rating": 1500, "Last Game Rating": 1878, "Rating Change": 378},
    {"Player": "nichiren1967", "Total Games": 1667, "First Game Rating": 1765, "Last Game Rating": 2008, "Rating Change": 243},
    {"Player": "german11", "Total Games": 1611, "First Game Rating": 1354, "Last Game Rating": 1590, "Rating Change": 236},
    {"Player": "cheesedout", "Total Games": 1452, "First Game Rating": 1827, "Last Game Rating": 1990, "Rating Change": 163},
    {"Player": "ChikiPuki", "Total Games": 1262, "First Game Rating": 1307, "Last Game Rating": 1649, "Rating Change": 342},
    {"Player": "Redneck", "Total Games": 1224, "First Game Rating": 1484, "Last Game Rating": 1615, "Rating Change": 131},
    {"Player": "Atomicangel", "Total Games": 1166, "First Game Rating": 1692, "Last Game Rating": 1962, "Rating Change": 270},
    {"Player": "Panevis", "Total Games": 1143, "First Game Rating": 2052, "Last Game Rating": 2092, "Rating Change": 40},
    {"Player": "Kiriush", "Total Games": 1097, "First Game Rating": 1238, "Last Game Rating": 1926, "Rating Change": 688},
    {"Player": "rashit49", "Total Games": 1072, "First Game Rating": 1370, "Last Game Rating": 1749, "Rating Change": 379},
    {"Player": "Messsi", "Total Games": 1066, "First Game Rating": 1749, "Last Game Rating": 1747, "Rating Change": -2},
    {"Player": "Oz", "Total Games": 932, "First Game Rating": 1500, "Last Game Rating": 1713, "Rating Change": 213},
    {"Player": "kent777", "Total Games": 916, "First Game Rating": 1756, "Last Game Rating": 2055, "Rating Change": 299},
    {"Player": "rapitrance", "Total Games": 907, "First Game Rating": 1602, "Last Game Rating": 1541, "Rating Change": -61},
    {"Player": "jack0211", "Total Games": 871, "First Game Rating": 1715, "Last Game Rating": 1624, "Rating Change": -91},
    {"Player": "Greenlan", "Total Games": 869, "First Game Rating": 1332, "Last Game Rating": 1742, "Rating Change": 410},
    {"Player": "ptdhina", "Total Games": 857, "First Game Rating": 1436, "Last Game Rating": 1548, "Rating Change": 112},
    {"Player": "MihaSAH", "Total Games": 827, "First Game Rating": 1669, "Last Game Rating": 1711, "Rating Change": 42},
    {"Player": "oilmanesh", "Total Games": 827, "First Game Rating": 1482, "Last Game Rating": 1914, "Rating Change": 432},
    {"Player": "Karen_Armenia", "Total Games": 821, "First Game Rating": 1510, "Last Game Rating": 1715, "Rating Change": 205}
]


data_rating_increase = [
    {"Player": "we_chess_now", "Total Games": 20, "First Game Rating": 1226, "Last Game Rating": 2176, "Rating Change": 950},
    {"Player": "brahmsguitar", "Total Games": 9, "First Game Rating": 1500, "Last Game Rating": 2403, "Rating Change": 903},
    {"Player": "BadTouch", "Total Games": 32, "First Game Rating": 1087, "Last Game Rating": 1949, "Rating Change": 862},
    {"Player": "dbnp", "Total Games": 20, "First Game Rating": 1200, "Last Game Rating": 2007, "Rating Change": 807},
    {"Player": "zzzz11111111", "Total Games": 16, "First Game Rating": 1217, "Last Game Rating": 2024, "Rating Change": 807},
    {"Player": "BVS1959", "Total Games": 162, "First Game Rating": 1149, "Last Game Rating": 1940, "Rating Change": 791},
    {"Player": "thaliolhagi", "Total Games": 70, "First Game Rating": 1202, "Last Game Rating": 1992, "Rating Change": 790},
    {"Player": "pedroydeo", "Total Games": 15, "First Game Rating": 1424, "Last Game Rating": 2193, "Rating Change": 769},
    {"Player": "toyota", "Total Games": 68, "First Game Rating": 1248, "Last Game Rating": 1998, "Rating Change": 750},
    {"Player": "sumanuwekwek", "Total Games": 14, "First Game Rating": 1500, "Last Game Rating": 2248, "Rating Change": 748},
    {"Player": "YaserAhmady", "Total Games": 9, "First Game Rating": 1200, "Last Game Rating": 1942, "Rating Change": 742},
    {"Player": "dayli", "Total Games": 15, "First Game Rating": 1070, "Last Game Rating": 1810, "Rating Change": 740},
    {"Player": "kuduy3", "Total Games": 12, "First Game Rating": 1435, "Last Game Rating": 2145, "Rating Change": 710},
    {"Player": "sidneycrode", "Total Games": 361, "First Game Rating": 1444, "Last Game Rating": 2150, "Rating Change": 706},
    {"Player": "2013_January", "Total Games": 11, "First Game Rating": 1294, "Last Game Rating": 1982, "Rating Change": 688},
    {"Player": "Kiriush", "Total Games": 1097, "First Game Rating": 1238, "Last Game Rating": 1926, "Rating Change": 688},
    {"Player": "jhericjared", "Total Games": 29, "First Game Rating": 1500, "Last Game Rating": 2185, "Rating Change": 685},
    {"Player": "WormHole", "Total Games": 529, "First Game Rating": 1280, "Last Game Rating": 1963, "Rating Change": 683},
    {"Player": "Glaile", "Total Games": 12, "First Game Rating": 1261, "Last Game Rating": 1938, "Rating Change": 677},
    {"Player": "Dirhby", "Total Games": 13, "First Game Rating": 1500, "Last Game Rating": 2176, "Rating Change": 676}
]


# Convert the lists of dictionaries to pandas DataFrames
df_games = pd.DataFrame(data_games)
df_rating_increase = pd.DataFrame(data_rating_increase)

# Function to render a DataFrame as a table image
def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = table(ax, data, bbox=bbox, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0] % len(row_colors)])
    return ax.get_figure(), ax

# Create a table image for top 20 players by number of games
fig_games, ax_games = render_mpl_table(df_games, header_columns=0, col_width=2.0)
plt.savefig(r'C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\src\visualization\top_20_players_by_games.png')

# Create a table image for top 20 players by rating increase
fig_rating_increase, ax_rating_increase = render_mpl_table(df_rating_increase, header_columns=0, col_width=2.0)
plt.savefig(r'C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\src\visualization\top_20_players_by_rating_increase.png')

plt.close(fig_games)
plt.close(fig_rating_increase)


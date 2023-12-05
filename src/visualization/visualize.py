import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Database path
db_path = r'C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\processed\lichess_13_01.db'


## query to find the rating over time (the highest rating of every day) for the top 20 players with the most games played

# Create a connection to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query_1 = '''
WITH PlayerGames AS (
    SELECT white_player AS player, game_date, white_elo AS elo
    FROM games
    UNION ALL
    SELECT black_player, game_date, black_elo
    FROM games
),
RankedPlayers AS (
    SELECT player, COUNT(*) AS games_played
    FROM PlayerGames
    GROUP BY player
    ORDER BY games_played DESC
    LIMIT 20
),
DailyMaxRating AS (
    SELECT pg.player, pg.game_date, MAX(pg.elo) AS daily_max_elo
    FROM PlayerGames pg
    INNER JOIN RankedPlayers rp ON pg.player = rp.player
    GROUP BY pg.player, pg.game_date
),
RatingWithCarryOver AS (
    SELECT 
        dmr.player, 
        dmr.game_date, 
        dmr.daily_max_elo,
        COALESCE(
            dmr.daily_max_elo, 
            (SELECT daily_max_elo FROM DailyMaxRating WHERE player = dmr.player AND game_date < dmr.game_date ORDER BY game_date DESC LIMIT 1)
        ) AS adjusted_elo
    FROM DailyMaxRating dmr
)
SELECT * FROM RatingWithCarryOver
ORDER BY player, game_date;
'''
## execute the query and fetch the results.
cursor.execute(query_1)
top_player_time_series = cursor.fetchall()

## plotting rating over time

# Convert the results to a pandas dataframe
df = pd.DataFrame(top_player_time_series, columns=['player', 'game_date', 'daily_max_elo', 'adjusted_elo'])

# Convert the game_date column to a datetime object
df['game_date'] = pd.to_datetime(df['game_date'])

# Calculate the moving average (smoothed Elo)
N = 3  # Window size for moving average
df['smoothed_elo'] = df.groupby('player')['adjusted_elo'].transform(lambda x: x.rolling(window=N, min_periods=1).mean())

# Convert game_date from timestamp to numeric for regression
df['game_date_numeric'] = (df['game_date'] - df['game_date'].min()).dt.days

# Create a plot
sns.set_style('darkgrid')
fig, ax = plt.subplots(figsize=(12, 8))

# Adjusting the x-axis range
start_date = pd.to_datetime('2012-12-31')
end_date = pd.to_datetime('2013-01-31')
ax.set_xlim((start_date - df['game_date'].min()).days, (end_date - df['game_date'].min()).days)

# Plot the smoothed Elo ratings
sns.lineplot(data=df, x='game_date_numeric', y='smoothed_elo', ax=ax)

# Add a regression line
sns.regplot(data=df, x='game_date_numeric', y='smoothed_elo', scatter=False, ax=ax, color='black', label='Regression Line')

# Set plot details
ax.set_title('Smoothed Rating Evolution of Top 20 Players by Number of Games Played')
ax.set_xlabel('Date')
ax.set_ylabel('Rating')
ax.set_xlim((start_date - df['game_date'].min()).days, (end_date - df['game_date'].min()).days)
ax.set_xticks([(start_date + pd.Timedelta(days=i) - df['game_date'].min()).days for i in range((end_date - start_date).days + 1)])
ax.set_xticklabels([(start_date + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)], rotation=45)

## add player names to the plot

# Extract unique players from the dataframe
unique_players = df['player'].unique()

# Generate a color palette for the unique players
palette = sns.color_palette("tab20", n_colors=len(unique_players))
player_palette = dict(zip(unique_players, palette))

# Plot each player's smoothed Elo ratings with the corresponding color
for player, group in df.groupby('player'):
    sns.lineplot(x='game_date_numeric', y='smoothed_elo', data=group, label=player, ax=ax, color=player_palette[player])

# Now add the player names at the start and end of each line
for player, group in df.groupby('player'):
    start_point = group.iloc[0]
    end_point = group.iloc[-1]
    ax.text(x=start_point['game_date_numeric'], y=start_point['smoothed_elo'], s=player, color=player_palette[player], ha='right', va='center', fontsize=9)
    ax.text(x=end_point['game_date_numeric'], y=end_point['smoothed_elo'], s=player, color=player_palette[player], ha='left', va='center', fontsize=9)

# Other parts of the code remain unchanged
# Move the legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(-0.31, 1))
plt.show()

# close connection
conn.close()
# Lichess ETL Pipeline Project

## Project Overview
This project involved developing an ETL (Extract, Transform, Load) pipeline to analyze chess game data from Lichess. The goal was to extract game data, perform transformations to derive insights, and load the data into a SQLite database for analysis.

## Methodology
- Extracted and decompressed data from Lichess in PGN (Portable Game Notation) format.
- Transformed data using Python to calculate player ratings and game outcomes.
- Loaded the data into a SQLite database and used SQL queries for further faster analysis.
- Visualized the data using Seaborn in Python to understand the rating evolution of players.

## Key Findings
- Identified the top 20 players by the number of games played and by rating increase.
- Analyzed the rating evolution over time, revealing patterns in player performance and activity.

## Smoothed Rating Evolution Graph
![output](https://github.com/magellanic-clouds17/etl_pipeline_lichess/assets/72970703/098efd18-fe6d-4e6a-a923-d0d010d7bdbe)

*The graph illustrates the smoothed rating evolution over time for the top 20 players. Each line represents a player's rating change from the first to the last game of January 2013. The graph highlights the dynamic nature of player ratings and showcases significant improvements or declines.*

## Conclusion
The project successfully provided insights into the playing habits and performance trends of Lichess players, demonstrating my knowledge of data engineering to transform raw data into meaningful information.

## Top Players Analysis
- **F1_ALONSO_FERRARI**: Played the most games, with a total of 1729 games and an overall rating increase of 378 points.
- **Kiriush**: Had the highest rating increase of 688 points across 1097 games.

### Top 20 Players by Rating increase:

![top_20_players_by_rating_increase](https://github.com/magellanic-clouds17/etl_pipeline_lichess/assets/72970703/d573ba31-93c9-4382-8b04-48469c495b33)


### Top 20 Players by Number of Games:

![top_20_players_by_games](https://github.com/magellanic-clouds17/etl_pipeline_lichess/assets/72970703/a54ec481-f950-4bbf-b9d3-0ab1f618e9c6)

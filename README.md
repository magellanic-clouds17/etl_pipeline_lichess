# Lichess ETL Pipeline Project

## Project Overview
This project involved developing an ETL (Extract, Transform, Load) pipeline to analyze chess game data from Lichess. The goal was to extract game data, perform transformations to derive insights, and load the data into a SQLite database for analysis.

## Methodology
- Extracted data from Lichess in PGN (Portable Game Notation) format.
- Transformed data using Python to calculate player ratings and game outcomes.
- Loaded the data into a SQLite database and used SQL queries for further analysis.
- Visualized the data using Seaborn in Python to understand the rating evolution of players.

## Key Findings
- Identified the top 20 players by the number of games played and by rating increase.
- Analyzed the rating evolution over time, revealing patterns in player performance and activity.

## Smoothed Rating Evolution Graph
![output](https://github.com/magellanic-clouds17/etl_pipeline_lichess/assets/72970703/098efd18-fe6d-4e6a-a923-d0d010d7bdbe)

*The graph illustrates the smoothed rating evolution over time for the top 20 players. Each line represents a player's rating change from the first to the last game of January 2013. The graph highlights the dynamic nature of player ratings and showcases significant improvements or declines.*

## Conclusion
The project successfully provided insights into the playing habits and performance trends of Lichess players, demonstrating the power of data engineering in transforming raw data into meaningful information.

## Top Players Analysis
- **F1_ALONSO_FERRARI**: Played the most games, with a total of 1729 games and an overall rating increase of 378 points.
- **Kiriush**: Had the highest rating increase of 688 points across 1097 games.

### Top 20 Players by Rating increase:

Player: we_chess_now
Total Games: 20
First Game: 2013.01.02, Rating: 1226
Last Game: 2013.01.05, Rating: 2176
Rating Change: 950

Player: brahmsguitar
Total Games: 9
First Game: 2013.01.10, Rating: 1500
Last Game: 2013.01.11, Rating: 2403
Rating Change: 903

Player: BadTouch
Total Games: 32
First Game: 2013.01.04, Rating: 1087
Last Game: 2013.01.04, Rating: 1949
Rating Change: 862

Player: dbnp
Total Games: 20
First Game: 2013.01.01, Rating: 1200
Last Game: 2013.01.19, Rating: 2007
Rating Change: 807

Player: zzzz11111111
Total Games: 16
First Game: 2013.01.03, Rating: 1217
Last Game: 2013.01.13, Rating: 2024
Rating Change: 807

Player: BVS1959
Total Games: 162
First Game: 2013.01.23, Rating: 1149
Last Game: 2013.01.31, Rating: 1940
Rating Change: 791

Player: thaliolhagi
Total Games: 70
First Game: 2013.01.24, Rating: 1202
Last Game: 2013.01.25, Rating: 1992
Rating Change: 790

Player: pedroydeo
Total Games: 15
First Game: 2013.01.09, Rating: 1424
Last Game: 2013.01.09, Rating: 2193
Rating Change: 769

Player: toyota
Total Games: 68
First Game: 2013.01.03, Rating: 1248
Last Game: 2013.01.03, Rating: 1998
Rating Change: 750

Player: sumanuwekwek
Total Games: 14
First Game: 2013.01.27, Rating: 1500
Last Game: 2013.01.27, Rating: 2248
Rating Change: 748

Player: YaserAhmady
Total Games: 9
First Game: 2013.01.29, Rating: 1200
Last Game: 2013.01.30, Rating: 1942
Rating Change: 742

Player: dayli
Total Games: 15
First Game: 2013.01.30, Rating: 1070
Last Game: 2013.01.31, Rating: 1810
Rating Change: 740

Player: kuduy3
Total Games: 12
First Game: 2013.01.14, Rating: 1435
Last Game: 2013.01.14, Rating: 2145
Rating Change: 710

Player: sidneycrode
Total Games: 361
First Game: 2013.01.03, Rating: 1444
Last Game: 2013.01.31, Rating: 2150
Rating Change: 706

Player: 2013_January
Total Games: 11
First Game: 2013.01.01, Rating: 1294
Last Game: 2013.01.01, Rating: 1982
Rating Change: 688

Player: Kiriush
Total Games: 1097
First Game: 2013.01.11, Rating: 1238
Last Game: 2013.01.31, Rating: 1926
Rating Change: 688

Player: jhericjared
Total Games: 29
First Game: 2013.01.08, Rating: 1500
Last Game: 2013.01.09, Rating: 2185
Rating Change: 685

Player: WormHole
Total Games: 529
First Game: 2013.01.03, Rating: 1280
Last Game: 2013.01.23, Rating: 1963
Rating Change: 683

Player: Glaile
Total Games: 12
First Game: 2013.01.16, Rating: 1261
Last Game: 2013.01.16, Rating: 1938
Rating Change: 677

Player: Dirhby
Total Games: 13
First Game: 2013.01.14, Rating: 1500
Last Game: 2013.01.14, Rating: 2176
Rating Change: 676


### Top 20 Players by Number of Games:

	Player: *F1_ALONSO_FERRARI*
Total Games: 1729
First Game: 2013.01.02, Rating: 1500
Last Game: 2013.01.31, Rating: 1878
Rating Change: 378

Player: nichiren1967
Total Games: 1667
First Game: 2012.12.31, Rating: 1765
Last Game: 2013.01.31, Rating: 2008
Rating Change: 243

Player: german11
Total Games: 1611
First Game: 2013.01.01, Rating: 1354
Last Game: 2013.01.31, Rating: 1590
Rating Change: 236

Player: cheesedout
Total Games: 1452
First Game: 2012.12.31, Rating: 1827
Last Game: 2013.01.30, Rating: 1990
Rating Change: 163

Player: ChikiPuki
Total Games: 1262
First Game: 2013.01.01, Rating: 1307
Last Game: 2013.01.31, Rating: 1649
Rating Change: 342

Player: Redneck
Total Games: 1224
First Game: 2013.01.02, Rating: 1484
Last Game: 2013.01.19, Rating: 1615
Rating Change: 131

Player: Atomicangel
Total Games: 1166
First Game: 2013.01.01, Rating: 1692
Last Game: 2013.01.31, Rating: 1962
Rating Change: 270

Player: Panevis
Total Games: 1143
First Game: 2013.01.01, Rating: 2052
Last Game: 2013.01.31, Rating: 2092
Rating Change: 40

Player: Kiriush
Total Games: 1097
First Game: 2013.01.11, Rating: 1238
Last Game: 2013.01.31, Rating: 1926
Rating Change: 688

Player: rashit49
Total Games: 1072
First Game: 2013.01.01, Rating: 1370
Last Game: 2013.01.31, Rating: 1749
Rating Change: 379

Player: Messsi
Total Games: 1066
First Game: 2013.01.01, Rating: 1749
Last Game: 2013.01.30, Rating: 1747
Rating Change: -2

Player: Oz
Total Games: 932
First Game: 2013.01.05, Rating: 1500
Last Game: 2013.01.31, Rating: 1713
Rating Change: 213

Player: kent777
Total Games: 916
First Game: 2013.01.01, Rating: 1756
Last Game: 2013.01.31, Rating: 2055
Rating Change: 299

Player: rapitrance
Total Games: 907
First Game: 2013.01.04, Rating: 1602
Last Game: 2013.01.31, Rating: 1541
Rating Change: -61

Player: jack0211
Total Games: 871
First Game: 2013.01.01, Rating: 1715
Last Game: 2013.01.29, Rating: 1624
Rating Change: -91

Player: Greenlan
Total Games: 869
First Game: 2013.01.23, Rating: 1332
Last Game: 2013.01.31, Rating: 1742
Rating Change: 410

Player: ptdhina
Total Games: 857
First Game: 2013.01.01, Rating: 1436
Last Game: 2013.01.31, Rating: 1548
Rating Change: 112

Player: MihaSAH
Total Games: 827
First Game: 2013.01.01, Rating: 1669
Last Game: 2013.01.31, Rating: 1711
Rating Change: 42

Player: oilmanesh
Total Games: 827
First Game: 2013.01.01, Rating: 1482
Last Game: 2013.01.31, Rating: 1914
Rating Change: 432

Player: Karen_Armenia
Total Games: 821
First Game: 2013.01.01, Rating: 1510
Last Game: 2013.01.31, Rating: 1715
Rating Change: 205



from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Nikola Jokic
career = playercareerstats.PlayerCareerStats(player_id='203999');
# pandas data frames (optional: pip install pandas)

# Get Nikola Jokic's total stats
totals = career.season_totals_regular_season.get_data_frame();

print ("\nNikola Jokic's career stats:\n", totals);
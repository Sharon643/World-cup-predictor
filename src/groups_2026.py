import pandas as pd
from pathlib import Path
from src.group_stage import simulate_group

BASE_DIR = Path(__file__).resolve().parent.parent

TEAM_STATS_PATH = (
    BASE_DIR /
    "data" /
    "team_stats.csv"
)
GROUPS = {
    "A": ["Mexico", "Czech Republic", "South Africa", "South Korea"],
    "B": ["Canada", "Switzerland", "Bosnia and Herzegovina", "Qatar"],
    "C": ["Brazil", "Morocco", "Scotland", "Haiti"],
    "D": ["United States", "Turkey", "Australia", "Paraguay"],
    "E": ["Germany", "Ivory Coast", "Ecuador", "Curaçao"],
    "F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
    "G": ["Belgium", "Iran", "Egypt", "New Zealand"],
    "H": ["Spain", "Uruguay", "Saudi Arabia", "Cape Verde"],
    "I": ["France", "Senegal", "Norway", "Iraq"],
    "J": ["Argentina", "Algeria", "Austria", "Jordan"],
    "K": ["Portugal", "Colombia", "DR Congo", "Uzbekistan"],
    "L": ["England", "Croatia", "Ghana", "Panama"],
}
team_stats = pd.read_csv(
    TEAM_STATS_PATH
)
team_stats = team_stats.set_index("team")

all_teams = []

for teams in GROUPS.values():
    all_teams.extend(teams)

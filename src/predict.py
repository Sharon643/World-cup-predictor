from pathlib import Path
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR /
    "models" /
    "world_cup_predictor.pkl"
)

TEAM_STATS_PATH = (
    BASE_DIR /
    "data" /
    "team_stats.csv"
)

xgb = joblib.load(MODEL_PATH)

team_stats = pd.read_csv(
    TEAM_STATS_PATH
)
team_stats = team_stats.set_index("team")
def predict_match(
    home_team,
    away_team,
    neutral=1,
    tournament_type="world_cup"
):

    home = team_stats.loc[home_team]

    away = team_stats.loc[away_team]

    form_diff = (
        home["form"]
        - away["form"]
    )

    goal_diff_diff = (
        home["goal_diff"]
        - away["goal_diff"]
    )

    scored_diff = (
        home["avg_scored"]
        - away["avg_scored"]
    )

    conceded_diff = (
        home["avg_conceded"]
        - away["avg_conceded"]
    )

    elo_diff = (
        home["elo"]
        - away["elo"]
    )

    tournament_features = {

        "tournament_type_continental_qualifier": 0,
        "tournament_type_friendly": 0,
        "tournament_type_nations_league": 0,
        "tournament_type_other": 0,
        "tournament_type_regional": 0,
        "tournament_type_world_cup": 0,
        "tournament_type_world_cup_qualifier": 0

    }
    column = (
        f"tournament_type_{tournament_type}"
    )

    if column in tournament_features:

        tournament_features[column] = 1

    features = {

        "form_diff": form_diff,

        "goal_diff_diff":
            goal_diff_diff,

        "scored_diff":
            scored_diff,

        "conceded_diff":
            conceded_diff,

        "elo_diff":
            elo_diff,

        "neutral":
            neutral
    }

    features.update(
        tournament_features
    )
    match_df = pd.DataFrame([features])
    probs = xgb.predict_proba(match_df)[0]
    return {
    "home_win": float(round(probs[0] * 100, 2)),
    "draw": float(round(probs[1] * 100, 2)),
    "away_win": float(round(probs[2] * 100, 2))
    }

from predict import predict_match
from score_generator import generate_score
from predict import team_stats

import random

def simulate_match(home_team,away_team,neutral=1,tournament_type="world_cup"):

    probs = predict_match(
        home_team,
        away_team,
        neutral,
        tournament_type
    )

    outcome = random.choices(

        [
            "home_win",
            "draw",
            "away_win"
        ],

        weights=[
            probs["home_win"],
            probs["draw"],
            probs["away_win"]
        ],

        k=1

    )[0]

    home_stats = team_stats.loc[home_team]

    away_stats = team_stats.loc[away_team]

    home_score, away_score = generate_score(outcome,home_stats,away_stats)

    return {

        "home_team": home_team,

        "away_team": away_team,

        "home_score": home_score,

        "away_score": away_score,

        "outcome": outcome,

        "probabilities": probs

    }


results = {
    "home_win": 0,
    "draw": 0,
    "away_win": 0
}

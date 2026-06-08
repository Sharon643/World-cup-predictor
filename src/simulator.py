from predict import predict_match

import random

def simulate_match(
    home_team,
    away_team,
    neutral=1,
    tournament_type="world_cup"
):

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

    return {

        "home_team": home_team,

        "away_team": away_team,

        "outcome": outcome,

        "probabilities": probs

    }


results = {
    "home_win": 0,
    "draw": 0,
    "away_win": 0
}

for _ in range(10000):

    result = simulate_match(
        "Argentina",
        "France"
    )

    results[
        result["outcome"]
    ] += 1

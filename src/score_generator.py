import numpy as np


def generate_score(outcome,home_stats,away_stats):

    home_expected = (home_stats["avg_scored"]+away_stats["avg_conceded"]) / 2 * 0.7

    away_expected = (away_stats["avg_scored"]+home_stats["avg_conceded"]) / 2 *0.7

    home_goals = max(0,round(np.random.normal(home_expected,1)))

    away_goals = max(0,round(np.random.normal(away_expected,1)))

    if outcome == "home_win":

        while home_goals <= away_goals:

            home_goals += 1

    elif outcome == "away_win":

        while away_goals <= home_goals:

            away_goals += 1

    else:

        average_goals = round((home_expected+away_expected) / 2)

        home_goals = average_goals
        away_goals = average_goals
    
    return home_goals, away_goals
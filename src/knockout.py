from src.simulator import simulate_match
import random

def simulate_knockout_match(team1,team2):
    result = simulate_match(team1,team2)
    if result["outcome"] == "draw":

        winner = random.choice(
            [team1, team2]
        )

    elif result["outcome"] == "home_win":

        winner = team1

    else:

        winner = team2

    return {

        "team1": team1,

        "team2": team2,

        "winner": winner,

        "result": result

    }

def simulate_knockout_round(teams):
    winners = []

    matches = []

    for i in range(0,len(teams),2):
        team1 = teams[i]

        team2 = teams[i + 1]

        match = simulate_knockout_match(team1,team2)

        winners.append(match["winner"])

        matches.append(match)

    return {

        "winners": winners,

        "matches": matches

    }
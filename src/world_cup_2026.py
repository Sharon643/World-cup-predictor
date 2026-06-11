from group_stage import simulate_group
from groups_2026 import GROUPS
from knockout import simulate_knockout_round
import random


def simulate_group_stage_2026(groups):

    group_results = {}

    winners = []
    runners_up = []
    third_place = []

    for group_name, teams in groups.items():

        standings = simulate_group(teams)

        group_results[group_name] = standings

        # Top 2 automatically qualify
        winners.append(standings[0])
        runners_up.append(standings[1])

        # Save 3rd place team
        third_place.append(standings[2])

    # Sort 3rd place teams
    third_place = sorted(
        third_place,
        key=lambda x: (
            x[1]["points"],
            x[1]["gd"],
            x[1]["gf"]
        ),
        reverse=True
    )

    # Best 8 third-place teams
    best_third_place = third_place[:8]

    qualified_teams = []

    for team, stats in winners:
        qualified_teams.append(team)

    for team, stats in runners_up:
        qualified_teams.append(team)

    for team, stats in best_third_place:
        qualified_teams.append(team)
    

    return {
        "group_results": group_results,
        "winners": winners,
        "runners_up": runners_up,
        "best_third_place": best_third_place,
        "qualified_teams": qualified_teams
    }



def simulate_world_cup_2026():

    results = simulate_group_stage_2026(
        GROUPS
    )

    winners = {
        chr(65 + i): results["winners"][i][0]
        for i in range(12)
    }

    runners = {
        chr(65 + i): results["runners_up"][i][0]
        for i in range(12)
    }

    third = [
        team
        for team, _ in results["best_third_place"]
    ]
    r32_teams = [

        runners["A"], runners["B"],

        winners["C"], runners["F"],

        winners["E"], third[0],

        winners["F"], runners["C"],

        runners["E"], runners["I"],

        winners["I"], third[1],

        winners["A"], third[2],

        winners["L"], third[3],

        winners["G"], third[4],

        winners["D"], third[5],

        winners["H"], runners["J"],

        runners["K"], runners["L"],

        winners["J"], runners["H"],

        winners["B"], third[6],

        runners["D"], runners["G"],

        winners["K"], third[7]

    ]


    r32 = simulate_knockout_round(
        r32_teams
    )

    r16 = simulate_knockout_round(
        r32["winners"]
    )

    qf = simulate_knockout_round(
        r16["winners"]
    )

    sf = simulate_knockout_round(
        qf["winners"]
    )

    final = simulate_knockout_round(
        sf["winners"]
    )
    # print("\nROUND OF 32")

    # for match in r32["matches"]:
    #     print(
    #         f"{match['team1']} vs {match['team2']}"
    #     )

    # print("\nROUND OF 16")

    # for match in r16["matches"]:
    #     print(
    #         f"{match['team1']} vs {match['team2']}"
    #     )
    # print("\nQUARTERFINALS")

    # for match in qf["matches"]:
    #     print(
    #         f"{match['team1']} vs {match['team2']}"
    #     )
    # print("\nSEMIFINALS")

    # for match in sf["matches"]:
    #     print(
    #         f"{match['team1']} vs {match['team2']}"
    #     )
    #     print("\nFINAL")

    # for match in final["matches"]:
    #     print(
    #         f"{match['team1']} vs {match['team2']}"
    #     )

    return final["winners"][0]

champions = {}

for _ in range(500):

    champion = simulate_world_cup_2026()

    champions[champion] = (
        champions.get(champion, 0) + 1
    )
print("Winner :", champion)
print("\nChampionship Rates\n")
for team, wins in sorted(champions.items(),key=lambda x: x[1],reverse=True):

    print(team,round(wins / 500 * 100,2),"%")

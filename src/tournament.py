from src.group_stage import simulate_group

def simulate_group_stage(groups):

    group_results = {}

    qualified_teams = []

    for group_name, teams in groups.items():

        standings = simulate_group(
            teams
        )

        qualifiers = [

            standings[0][0],
            standings[1][0]
        ]

        qualified_teams.extend(
            qualifiers
        )

        group_results[group_name] = {

            "standings": standings,

            "winner": standings[0][0],

            "runner_up": standings[1][0]
        }

    return {

        "group_results": group_results,

        "qualified_teams": qualified_teams
    }

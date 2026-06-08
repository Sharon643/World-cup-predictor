from simulator import simulate_match



def create_table(teams):

    table = {}

    for team in teams:

        table[team] = {

            "points": 0,

            "wins": 0,

            "draws": 0,

            "losses": 0
        }

    return table

def generate_group_matches(teams):

    matches = []

    for i in range(len(teams)):

        for j in range(i + 1, len(teams)):

            matches.append(
                (teams[i], teams[j])
            )

    return matches



def update_table(
    table,
    home_team,
    away_team,
    outcome
):

    if outcome == "home_win":

        table[home_team]["points"] += 3
        table[home_team]["wins"] += 1

        table[away_team]["losses"] += 1

    elif outcome == "away_win":

        table[away_team]["points"] += 3
        table[away_team]["wins"] += 1

        table[home_team]["losses"] += 1

    else:

        table[home_team]["points"] += 1
        table[away_team]["points"] += 1

        table[home_team]["draws"] += 1
        table[away_team]["draws"] += 1

def simulate_group(teams):

    table = create_table(teams)

    fixtures = generate_group_matches(
        teams
    )

    for home_team, away_team in fixtures:

        result = simulate_match(
            home_team,
            away_team
        )

        update_table(

            table,

            home_team,

            away_team,

            result["outcome"]

        )

    standings = sorted(

        table.items(),

        key=lambda x: x[1]["points"],

        reverse=True

    )

    return standings

group = [

    "Argentina",

    "France",

    "Japan",

    "Mexico"
]

standings = simulate_group(group)

for team, stats in standings:

    print(team, stats)
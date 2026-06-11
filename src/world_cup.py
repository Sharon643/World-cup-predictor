from tournament import simulate_group_stage
from knockout import simulate_knockout_round
from simulator import simulate_match

groups = {

    "A": [
        "Argentina",
        "France",
        "Japan",
        "Mexico"
    ],

    "B": [
        "Brazil",
        "Spain",
        "Morocco",
        "United States"
    ],

    "C": [
        "England",
        "Portugal",
        "Denmark",
        "South Korea"
    ],

    "D": [
        "Germany",
        "Netherlands",
        "Croatia",
        "Switzerland"
    ]
}
def create_knockout_bracket(group_results):

    A1 = group_results["A"]["winner"]
    A2 = group_results["A"]["runner_up"]

    B1 = group_results["B"]["winner"]
    B2 = group_results["B"]["runner_up"]

    C1 = group_results["C"]["winner"]
    C2 = group_results["C"]["runner_up"]

    D1 = group_results["D"]["winner"]
    D2 = group_results["D"]["runner_up"]

    return [

        A1, B2,

        B1, A2,

        C1, D2,

        D1, C2

    ]
def simulate_world_cup():
    group_results = simulate_group_stage(groups)
    
    quarterfinalists = create_knockout_bracket(group_results["group_results"])

    quarterfinals = simulate_knockout_round(quarterfinalists)
    semifinals = simulate_knockout_round(quarterfinals["winners"])

    final = simulate_knockout_round(semifinals["winners"])

    champion = final["winners"][0]
    return champion


champions = {}

qualification_counts = {}

for _ in range(500):
    results = simulate_group_stage(groups)
    for team in results["qualified_teams"]:

        qualification_counts[team] = (
            qualification_counts.get(team, 0) + 1
        )
    


    champion = simulate_world_cup()

    champions[champion] = (champions.get(champion,0) + 1)
print("\nQualification Rates\n")
for team, count in sorted(qualification_counts.items(),key=lambda x: x[1],reverse=True):

    print(
            team,
            round(count / 500 * 100, 1),
            "%"
        )
print("\nChampionship Rates\n")
for team, wins in sorted(champions.items(),key=lambda x: x[1],reverse=True):

    print(team,round(wins / 500 * 100,2),"%")





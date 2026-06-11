import streamlit as st
import pandas as pd
from src.predict import predict_match
from src.world_cup_2026 import run_monte_carlo
from src.world_cup_2026 import simulate_world_cup_2026


def predict_score(team1, team2):
    
    home = team_stats.loc[team1]
    away = team_stats.loc[team2]

    home_goals = round(
        (
            home["avg_scored"]
            + away["avg_conceded"]
        ) / 2
    )

    away_goals = round(
        (
            away["avg_scored"]
            + home["avg_conceded"]
        ) / 2
    )

    return home_goals, away_goals

st.set_page_config(
    page_title="2026 World Cup Predictor",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ 2026 FIFA World Cup Predictor")

page = st.sidebar.radio(
    "Choose Page",
    [
        "Tournament Simulator",
        "World Cup Forecast",
        "Match Predictor"
        
    ]
)

if page == "Tournament Simulator":

    st.header("🏆 Tournament Simulator")

    st.write(
        "Simulate a complete 2026 FIFA World Cup."
    )

    if st.button("Simulate Tournament"):

        champion = simulate_world_cup_2026()

        st.success(
            f"🏆 Champion: {champion}"
        )

if page == "Match Predictor":

    st.header("Match Predictor")


    team_stats = pd.read_csv(
        "data/world_cup_2026_teams.csv"
    )

    teams = sorted(
        team_stats["team"].unique()
    )

    team1 = st.selectbox(
        "Home Team",
        teams
    )

    team2 = st.selectbox(
        "Away Team",
        teams
    )
    if st.button("Predict Match"):
        result = predict_match(
        team1,
        team2)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                team1,
                f"{result['home_win']:.1f}%"
            )

        with col2:
            st.metric(
                "Draw",
                f"{result['draw']:.1f}%"
            )

        with col3:
            st.metric(
                team2,
                f"{result['away_win']:.1f}%"
            )
        h, a = predict_score(team1, team2)

        st.subheader(
            f"Predicted Score: {team1} {h}-{a} {team2}"
        )

if page == "World Cup Forecast":

    st.header("2026 World Cup Forecast")
    
    num_sims = st.slider(
    "Number of Simulations",
    min_value=100,
    max_value=5000,
    value=500,
    step=100)
    if st.button("Run Forecast"):

        with st.spinner("Running Monte Carlo simulations..."):

            results = run_monte_carlo(num_sims)

        forecast_df = pd.DataFrame(
        results.items(),
        columns=[
            "Team",
            "Win Probability"] )
        forecast_df = (forecast_df.sort_values(
            "Win Probability",
            ascending=False))
        
        top_team = forecast_df.iloc[0]

        st.subheader("🏆 Most Likely Champion")

        st.metric(
            top_team["Team"],
            f"{top_team['Win Probability']:.2f}%"
        )
        
        st.dataframe(forecast_df)

        st.subheader("Championship Odds")

        st.bar_chart(
            forecast_df.head(10).set_index("Team")
        )
        


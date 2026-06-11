import streamlit as st
import pandas as pd
from src.predict import predict_match

st.set_page_config(
    page_title="2026 World Cup Predictor",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ 2026 FIFA World Cup Predictor")

page = st.sidebar.radio(
    "Choose Page",
    [
        "Match Predictor",
        "World Cup Forecast"
    ]
)

if page == "Match Predictor":

    st.header("Match Predictor")


    team_stats = pd.read_csv(
        "data/team_stats.csv"
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

        st.metric(
        "Home Win",
        f"{result['home_win']:.1f}%"
        )

        st.metric(
            "Draw",
            f"{result['draw']:.1f}%"
        )

        st.metric(
            "Away Win",
            f"{result['away_win']:.1f}%"
        )

if page == "World Cup Forecast":

    st.header(
        "2026 World Cup Forecast"
    )
    if st.button("Run Simulation"):
        results = run_monte_carlo(500)

        forecast_df = pd.DataFrame(
        results.items(),
        columns=[
            "Team",
            "Win Probability"] )
        
        forecast_df = (forecast_df.sort_values(
            "Win Probability",
            ascending=False))
        
        st.dataframe(forecast_df)

        st.bar_chart(forecast_df.set_index("Team"))
        


# ⚽ 2026 FIFA World Cup Predictor

An end-to-end Machine Learning project that predicts international football match outcomes and simulates the 2026 FIFA World Cup using Elo ratings, XGBoost, and Monte Carlo simulations.

## 🚀 Features

* Predicts match outcomes (Home Win, Draw, Away Win)
* Custom Elo rating system for dynamic team strength evaluation
* Feature engineering using recent form, goal difference, goals scored, and goals conceded
* XGBoost multiclass classification model
* Full 2026 FIFA World Cup tournament simulation
* Group stage and knockout stage modeling
* Monte Carlo simulations for championship probability forecasting
* Interactive Streamlit dashboard

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Joblib

## 📊 Model Pipeline

Historical Match Data
→ Feature Engineering
→ Elo Ratings
→ XGBoost Classifier
→ Match Outcome Prediction
→ Tournament Simulation
→ Monte Carlo Forecasting

### Features Used

* Elo Rating
* Recent Form
* Goal Difference
* Average Goals Scored
* Average Goals Conceded

## 🏆 Tournament Simulator

The simulator models the complete 2026 FIFA World Cup format:

* 48 Teams
* 12 Groups
* Top 2 Teams from Each Group Qualify
* Best 8 Third-Placed Teams Qualify
* Round of 32
* Round of 16
* Quarterfinals
* Semifinals
* Final

Thousands of simulations are run to estimate championship probabilities for each nation.

## 📈 Example Forecast

| Team        | Championship Probability |
| ----------- | ------------------------ |
| Argentina   | 20.6%                    |
| Spain       | 22.6%                    |
| England     | 10.0%                    |
| Netherlands | 7.6%                     |
| Portugal    | 7.2%                     |

*Results vary depending on the number of simulations.*

## 💻 Streamlit Application

The dashboard includes:

### Match Predictor

Predicts the probability of:

* Home Win
* Draw
* Away Win

### World Cup Forecast

Runs Monte Carlo simulations and displays:

* Championship probabilities
* Team rankings
* Forecast visualizations

### Tournament Simulator

Simulates an entire FIFA World Cup and generates a tournament winner.

## 📂 Project Structure

```text
World-Cup-Predictor/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── matches.csv
│   └── team_stats.csv
│
├── models/
│   ├── world_cup_predictor.pkl
│   └── elo_ratings.pkl
│
└── src/
    ├── predict.py
    ├── simulator.py
    ├── group_stage.py
    ├── knockout.py
    ├── groups_2026.py
    └── world_cup_2026.py
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/world-cup-predictor.git
cd world-cup-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 🎯 Future Improvements

* Team logos and enhanced UI
* Score prediction using expected goals
* Interactive tournament bracket visualization
* Live FIFA ranking integration
* Automated data updates
* Player-level analytics

## 👨‍💻 Author

Sharon M

If you found this project interesting, consider giving it a ⭐ on GitHub.

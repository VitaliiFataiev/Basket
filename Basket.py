import streamlit as st

class BasketballGame:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score_team1 = 0
        self.score_team2 = 0

    def score(self, team, points):
        if team == 1:
            self.score_team1 += points
        elif team == 2:
            self.score_team2 += points

    def display_scoreboard(self):
        st.write("Scoreboard:")
        st.write(f"{self.team1}: {self.score_team1}")
        st.write(f"{self.team2}: {self.score_team2}")

def main():
    st.title("Basketball Game Tracker")

    team1_name = st.text_input("Enter name of Team 1")
    team2_name = st.text_input("Enter name of Team 2")

    game = BasketballGame(team1_name, team2_name)

    while True:
        choice = st.selectbox("Menu", ["Record score", "Display scoreboard", "Quit"])

        if choice == "Record score":
            team = st.selectbox("Enter team number", [1, 2])
            points = st.number_input("Enter points scored", value=0)
            game.score(team, points)
        elif choice == "Display scoreboard":
            game.display_scoreboard()
        elif choice == "Quit":
            st.write("Thanks for using the Basketball Game Tracker!")
            break

if __name__ == "__main__":
    main()

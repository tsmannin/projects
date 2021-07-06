#heres the main site to retrieve our data to see which teams are in which conference
nba_2017_season = "https://www.basketball-reference.com/leagues/NBA_2017.html"

def build_team_url(team):
    team.upper()
    team_url = "https://www.basketball-reference.com/teams/" + team + "/2017.html"
    return team_url

def build_player_url(first, last):
    first = first.lower()
    last = last.lower()
    player_url = "https://www.basketball-reference.com/players/" + last[0] + "/" + last[0:5] + first[0:2] + "01.html"
    return player_url

def main():
    lakers = build_team_url("LAL")
    print(lakers)
    chris = build_player_url("Chris", "Paul")
    print(chris)

if __name__ == "__main__":
    main()

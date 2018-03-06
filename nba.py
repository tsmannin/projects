#hey guys, heres the class structures for our project. maybe after Andre creates the functions to scrape the data, Hieu can create the csv files so that we can pass it into our main function to create our class objects easier?
#feel free to add more functions Tristan!



# conference class has two data attributes.
# name is string type
# teams is list type containing team objects
class Conference:
    def __init__(self, name, teams):
        self._name = name
        self._teams = teams
    def get_name(self):
        return self._name
    def get_teams(self):
        return self._teams
    def __str__(self):
        teams = self._teams[0]._name
        for team in self._teams[1:]:
            teams += ', ' + team._name
        return f"Name: {self._name}\nTeams: {teams}"

# team class has two data attributes.
# name is string type
# players is list type containing player objects
class Team:
    def __init__(self, name, players):
        self._name = name
        self._players = players
    def get_name(self):
        return self._name
    def get_players(self):
        return self._players
    def winning_percentage(self):
        pass

    #salary cap is adding all the players salary on the team for that year
    def salary_cap(self):
        pass
    def __str__(self):
        players = self._players[0]._name
        for player in self._players[1:]:
            players += ', ' + player._name
        return f"Name: {self._name}\nPlayers: {players}"

# player class has four data attributes.
# name is string type
# ppg is float type
# apg is float type
# rpg is float type
class Player:
    def __init__(self, name, ppg, apg, rpg):
        self._name = name
        self._ppg = ppg
        self._apg = apg
        self._rpg = rpg
    def get_name(self):
        return self._name
    def get_ppg(self):
        return self._ppg
    def get_apg(self):
        return self._apg
    def get_rpg(self):
        return self._rpg
    def true_shooting(self):
        pass
    def defensive_rating(self):
        pass
    def __str__(self):
        return f"Name: {self._name}\nPPG: {self._ppg}\nAPG: {self._apg}\nRPG: {self._rpg}"


def main():
    kobe = Player("Kobe Bryant", 31.2, 5.2, 7.1)
    derek = Player("Derek Fisher", 19.7, 7.2, 4.6)
    chris = Player("Chris Paul", 25.5, 6.7, 4.2)
    blake = Player("Blake Griffin", 15.6, 2.4, 10.1)
    laker_players = [kobe, derek]
    clipper_players = [chris, blake]
    lakers = Team("Lakers", laker_players)
    clippers = Team("Clippers", clipper_players)
    west_teams = [lakers, clippers]
    west_conf = Conference("Western Conference", west_teams)
    print()
    print(kobe)
    print()
    print(lakers)
    print()
    print(west_conf)

if __name__ == "__main__":
    main()
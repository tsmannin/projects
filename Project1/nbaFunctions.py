#hey guys, heres the class structures for our project. maybe after Andre creates the functions to scrape the data,
#Hieu can create the csv files so that we can pass it into our main function to create our class objects easier?
#feel free to add more functions Tristan!



# conference class has two data attributes.
# name is string type
# teams is list type containing team objects
import csv

class Conference:
    def __init__(self, name, teams):
        self._name = name
        self._teams = teams

    def get_name(self):
        return self._name

    def get_teams(self):
        return self._teams

    def create_conf_csv(self):
        filename = self.get_name() + ".csv"
        with open(filename, 'w', newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(self.get_teams()[0])
            writer.writerow(self.get_teams()[1:])

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

    def create_team_csv(self):
        # not sure if headers is at 0 or name is
        filename = self.get_players()[1] + ".csv"
        with open(filename, 'w', newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(self.get_players()[0])
            writer.writerow(self.get_players()[1:])

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
    def __init__(self, player):
        self._player = player

    def get_player(self):
        return self._player

    def set_player(self, newPlayer):
        self._player = newPlayer

    def read_player_csv(self, playerCsv):
        pass

    def create_player_csv(self):
        # not sure if headers is at 0 or name is
        filename = self.get_player()[1] + ".csv"
        with open(filename, 'w', newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(self.get_player()[0])
            writer.writerow(self.get_player()[1:])

    def display(self):
        pass

    def __str__(self):
        #return f"Name: {self._name}\nPPG: {self._ppg}\nAPG: {self._apg}\nRPG: {self._rpg}"
        pass


def main():
    # kobe = Player("Kobe Bryant", 31.2, 5.2, 7.1)
    # derek = Player("Derek Fisher", 19.7, 7.2, 4.6)
    # chris = Player("Chris Paul", 25.5, 6.7, 4.2)
    # blake = Player("Blake Griffin", 15.6, 2.4, 10.1)
    # laker_players = [kobe, derek]
    # clipper_players = [chris, blake]
    # lakers = Team("Lakers", laker_players)
    # clippers = Team("Clippers", clipper_players)
    # west_teams = [lakers, clippers]
    # west_conf = Conference("Western Conference", west_teams)
    # print()
    # print(kobe)
    # print()
    # print(lakers)
    # print()
    # print(west_conf)
    header = ["a", "b"]
    c = ['Cole Aldrich', 'C', '28', 'MIN', '62', '0', '531', '45', '86', '.523', '0', '0', '',
    '45', '86', '.523', '.523', '15', '22', '.682', '51', '107', '158', '25', '25', '23', '17', '85', '105']
    g = Player(c)
    g.create_player_csv(header)

if __name__ == "__main__":
    main()
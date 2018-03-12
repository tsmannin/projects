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

    def display(self):
        team = selg.get_teams()
        string = ''
        for i in team[0]:
            string += '{message:{fill}{align}{width}}'.format(message=i, fill=' ', align='<', width=25)
        string += '\n'
        team[1].pop(4)
        for i in team[1:]:
            for j in i:
                string += '{message:{fill}{align}{width}}'.format(message=j, fill='', align='<', width=25)
            string += '\n'
        print(string)


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

    def display(self):
        team = self.get_players()
        string = ''
        team[0].pop(6)
        for i in team[0]:
            string += '{message:{fill}{align}{width}}'.format(message=i, fill=' ', align='<', width=23)
        string += '\n'
        for i in team[1:]:
            i.pop(6)
        for j, c in enumerate(i):
            string += '{message:{fill}{align}{width}}'.format(message=c, fill='', align='<', width=23)
        string += '\n'
        print(string)


# player class has one data attribute.
# player is a list of a player's stats

class Player:
    def __init__(self, player):
        self._player = player

    def get_player(self):
        return self._player

    def set_player(self, newPlayer):
        self._player = newPlayer

    def update_player_csv(self, playerCsv, updateCat):
         # Read in the CSV data
        with open(playerCsv, 'r', newline = "") as f:
            reader = csv.DictReader(f)
            data = list(reader)
            headers = reader.fieldnames
            print(data)

        # Write back in the CSV file
        with open(playerCsv, 'w', newline = "") as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            for row in data:
                if row.values() == updateCat:
                    user = input("Updating " + updateCat + " category. Enter new data: ")
                    row[updateCat] = str(user)
                    writer.writerow(row)

    def create_player_csv(self):
        # not sure if headers is at 0 or name is
        filename = self.get_player()[1] + ".csv"
        with open(filename, 'w', newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(self.get_player()[0])
            writer.writerow(self.get_player()[1:])

    def display(self):
        team = self.get_player()
        string = ''
        for i in team[0]:
            string += '{message:{fill}{align}{width}}'.format(message=i, fill=' ', align='<', width=8)
        string += '\n'
        for i in team[1:]:
            string += '{message:{fill}{align}{width}}'.format(message=i, fill='', align='<', width=8)
        string += '\n'
        print(string)



# def main():
#     kobe = Player("Kobe Bryant", 31.2, 5.2, 7.1)
#     derek = Player("Derek Fisher", 19.7, 7.2, 4.6)
#     chris = Player("Chris Paul", 25.5, 6.7, 4.2)
#     blake = Player("Blake Griffin", 15.6, 2.4, 10.1)
#     laker_players = [kobe, derek]
#     clipper_players = [chris, blake]
#     lakers = Team("Lakers", laker_players)
#     clippers = Team("Clippers", clipper_players)
#     west_teams = [lakers, clippers]
#     west_conf = Conference("Western Conference", west_teams)
#     print()
#     print(kobe)
#     print()
#     print(lakers)
#     print()
#     print(west_conf)
#     header = ["a", "b"]
#     c = [header, 'Cole Aldrich', 'C', '28', 'MIN', '62', '0', '531', '45', '86', '.523', '0', '0', '0',
#     '45', '86', '.523', '.523', '15', '22', '.682', '51', '107', '158', '25', '25', '23', '17', '85', '105']
#     g = Player(c)
#     g.create_player_csv()
#     g.display()

# if __name__ == "__main__":
#     main()

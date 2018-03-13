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
        team = self.get_teams()
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

    def create_team_csv(self, team):
        team = team + ".csv"
        with open(team, 'w', newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(self.get_players()[0])
            for i in self.get_players()[1:]:
                writer.writerow([i][0])
                #writer.writerow()

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
    def __init__(self, name ,player):
        self._player = player
        self._name = name

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

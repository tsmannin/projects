from pathlib import Path
import nba as n
import scrape as s

nba_2017_season = "https://www.basketball-reference.com/leagues/NBA_2017.html"
teams = {'boston celtics': 'BOS', 'cleveland cavaliers' : 'CLE', 'toronto raptors' : 'TOR',
        'washington wizards':'WAS', 'atlanta hawks':'ATL', 'milwaukee bucks':'MIL',
        'indiana pacers':'IND','chicago bulls':'CHI','miami heat':'MIA','detroit pistons':'DET',
        'charlotte hornets':'CHA','new york knicks': 'NYK','orlando magic': 'ORL', 'philadelphia 76ers':'PHI',
        'brooklyn nets':'BKN','golden state warriors':"GSW",'san antonio spurs':'SAS','houston rockets':'HOU',
        'los angeles clippers':'LAC', 'utah jazz': 'UTA', 'oklahoma city thunder':'OKC','memphis grizzlies':'MEM',
        'portland trail blazers':'POR', 'denver nuggets':'DEN', 'new orleans pelicans':'NOP', 'dallas mavericks':'DAL',
        'sacramento kings':'SAC', 'minnesota timberwolves':'MIN', 'los angeles lakers':'LAL','phoenix suns':'PHX'}

#builds a url so we can look for that specific team
def build_team_url(team):
    values = teams.keys()
    team = team.lower()
    try:
        for key in values:
            if key.find(team) >= 0:#if you put maimi or just clippers it will give you the correct abreviation
                team = teams[key]
                return "https://www.basketball-reference.com/teams/" + team + "/2017.html"
        print("Sorry couldn't Find your team")
        return
    except KeyError:
        print("sorry No Team by That Na-me")
    except AttributeError:
        print("sorry No Team by That Name")
        
def build_player_url(first, last):
    first = first.lower()
    last = last.lower()
    player_url = "https://www.basketball-reference.com/players/" + last[0] + "/" + last[0:5] + first[0:2] + "01.html"
    return player_url

def nba_options():
    
    print("\n1. Conference")
    print("2. Team")
    print("3. Player")
    print("4. Back to main menu\n")
    choice = int(input("What would you like to do?\n"))
    return choice


def process_stats(choice):
    if choice == 1:
        #print conference stats here
        conf = input("Enter conference name: (East/West)")
        new_conf = n.Conference(conf, s.scrape_conference(conf))
        new_conf.display()
    elif choice == 2:
        #print team stats here
        team = input("Enter team name: ")
        url = build_team_url(team)
        if url:
            new_team = n.Team(team,s.scrape_team(url))
            new_team.display()
    elif choice == 3:
        #print player stats here
        player = input("Enter player name: (first name) (last name) and year (2016-17)")
        first,last,year = player.split()
        url = build_player_url(first, last)
        list_of_stats = s.scrape_player(url,year)
        player = n.Player(first + last,list_of_stats)
        player.display()
    elif choice == 4:
        pass

def process_csv_creation(choice):
    if choice == 1:
        #create csv file for conference
        conf = input("Enter conference name: (East/West)")
        myConf = n.Conference(conf, s.scrape_conference(conf))
        myConf.create_conf_csv()
    elif choice == 2:
        #create csv file for team
        team = input("Enter team name: ")
        url = build_team_url(team)
        myTeam = n.Team(team, s.scrape_team(url))
        myTeam.create_team_csv()
    elif choice == 3:
        #create csv file for player
        player = input("Enter player name: (first name) (last name) and year (2016-17)")
        first,last,year = player.split()
        url = build_player_url(first, last)
        myPlayer = n.Player(first + last,s.scrape_player(url,year))
        myPlayer.create_player_csv()
    elif choice == 4:
        pass

def store_file():
    savedir = Path('/home/ubuntu/workspace/python')
    if not savedir.exists():
        savedir.mkdir()
    file_name = input("What is the name of the file you want to store? (include the extension)")
    #file_name = savedir + Path(file_name)
    print("Where would you like to store the file?")
    choice = nba_options()
    if choice == 1:
        conference_path = savedir / Path("Conferences")
        if not conference_path.exists():
            conference_path.mkdir()
        file = list(savedir.glob(file_name))
        move_to = conference_path / Path(file_name)
        for f in file:
            f.rename(move_to)
    elif choice == 2:
        team_path = savedir / Path("Teams")
        if not team_path.exists():
            team_path.mkdir()
        file = list(savedir.glob(file_name))
        move_to = team_path / Path(file_name)
        for f in file:
            f.rename(move_to)
    elif choice == 3:
        player_path = savedir / Path("Players")
        if not player_path.exists():
            player_path.mkdir()
        file = list(savedir.glob(file_name))
        move_to = player_path / Path(file_name)
        for f in file:
            f.rename(move_to)
    elif choice == 4:
        pass
    
    
    
    
    
def main():
    choice = 0
    print("Hi. Welcome to our NBA stats filing system. What would you like to do?\n")
    while(choice != 4):
        print("\nMAIN MENU:")
        print("1. Get stats")
        print("2. Create csv files")
        print("3. Sort Files")
        print("4. Quit\n")
        
        try:
            choice = int(input("What would you like to do? \n"))
        except ValueError:
            print("\n\nPlease Enter A Valid Number\n")
        if choice == 1:
            print("\nWhat kind of stats would you like? ")
            choice = nba_options()
            if choice == 4:
                choice = 0
            else:
                process_stats(choice)
        elif choice == 2:
            print("\nWhat kind of csv file do you want to create? ")
            choice = nba_options()
            if choice == 4:
                choice = 0
            else:
                process_csv_creation(choice)
        elif choice == 3:
            #we need to find out what we want to update
            print("")
            store_file()
        elif choice == 4:
            print("GODDBYE!")
        



if __name__ == "__main__":
    main()from pathlib import Path
import nba as n
import scrape as s

nba_2017_season = "https://www.basketball-reference.com/leagues/NBA_2017.html"
teams = {'boston celtics': 'BOS', 'cleveland cavaliers' : 'CLE', 'toronto raptors' : 'TOR',
        'washington wizards':'WAS', 'atlanta hawks':'ATL', 'milwaukee bucks':'MIL',
        'indiana pacers':'IND','chicago bulls':'CHI','miami heat':'MIA','detroit pistons':'DET',
        'charlotte hornets':'CHA','new york knicks': 'NYK','orlando magic': 'ORL', 'philadelphia 76ers':'PHI',
        'brooklyn nets':'BKN','golden state warriors':"GSW",'san antonio spurs':'SAS','houston rockets':'HOU',
        'los angeles clippers':'LAC', 'utah jazz': 'UTA', 'oklahoma city thunder':'OKC','memphis grizzlies':'MEM',
        'portland trail blazers':'POR', 'denver nuggets':'DEN', 'new orleans pelicans':'NOP', 'dallas mavericks':'DAL',
        'sacramento kings':'SAC', 'minnesota timberwolves':'MIN', 'los angeles lakers':'LAL','phoenix suns':'PHX'}

#builds a url so we can look for that specific team
def build_team_url(team):
    values = teams.keys()
    team = team.lower()
    try:
        for key in values:
            if key.find(team) >= 0:#if you put maimi or just clippers it will give you the correct abreviation
                team = teams[key]
                return "https://www.basketball-reference.com/teams/" + team + "/2017.html"
        print("Sorry couldn't Find your team")
        return
    except KeyError:
        print("sorry No Team by That Na-me")
    except AttributeError:
        print("sorry No Team by That Name")
        
def build_player_url(first, last):
    first = first.lower()
    last = last.lower()
    player_url = "https://www.basketball-reference.com/players/" + last[0] + "/" + last[0:5] + first[0:2] + "01.html"
    return player_url

def nba_options():
    
    print("\n1. Conference")
    print("2. Team")
    print("3. Player")
    print("4. Back to main menu\n")
    choice = int(input("What would you like to do?\n"))
    return choice


def process_stats(choice):
    if choice == 1:
        #print conference stats here
        conf = input("Enter conference name: (East/West)")
        new_conf = n.Conference(conf, s.scrape_conference(conf))
        new_conf.display()
    elif choice == 2:
        #print team stats here
        team = input("Enter team name: ")
        url = build_team_url(team)
        if url:
            new_team = n.Team(team,s.scrape_team(url))
            new_team.display()
    elif choice == 3:
        #print player stats here
        player = input("Enter player name: (first name) (last name) and year (2016-17)")
        first,last,year = player.split()
        url = build_player_url(first, last)
        list_of_stats = s.scrape_player(url,year)
        player = n.Player(first + last,list_of_stats)
        player.display()
    elif choice == 4:
        pass

def process_csv_creation(choice):
    if choice == 1:
        #create csv file for conference
        conf = input("Enter conference name: (East/West)")
        myConf = n.Conference(conf, s.scrape_conference(conf))
        myConf.create_conf_csv()
    elif choice == 2:
        #create csv file for team
        team = input("Enter team name: ")
        url = build_team_url(team)
        myTeam = n.Team(team, s.scrape_team(url))
        myTeam.create_team_csv()
    elif choice == 3:
        #create csv file for player
        player = input("Enter player name: (first name) (last name) and year (2016-17)")
        first,last,year = player.split()
        url = build_player_url(first, last)
        myPlayer = n.Player(first + last,s.scrape_player(url,year))
        myPlayer.create_player_csv()
    elif choice == 4:
        pass

def store_file():
    savedir = Path('/home/ubuntu/workspace/python')
    if not savedir.exists():
        savedir.mkdir()
    file_name = input("What is the name of the file you want to store? (include the extension)")
    #file_name = savedir + Path(file_name)
    print("Where would you like to store the file?")
    choice = nba_options()
    if choice == 1:
        conference_path = savedir / Path("Conferences")
        if not conference_path.exists():
            conference_path.mkdir()
        file = list(savedir.glob(file_name))
        move_to = conference_path / Path(file_name)
        for f in file:
            f.rename(move_to)
    elif choice == 2:
        team_path = savedir / Path("Teams")
        if not team_path.exists():
            team_path.mkdir()
        file = list(savedir.glob(file_name))
        move_to = team_path / Path(file_name)
        for f in file:
            f.rename(move_to)
    elif choice == 3:
        player_path = savedir / Path("Players")
        if not player_path.exists():
            player_path.mkdir()
        file = list(savedir.glob(file_name))
        move_to = player_path / Path(file_name)
        for f in file:
            f.rename(move_to)
    elif choice == 4:
        pass
    
    
    
    
    
def main():
    choice = 0
    print("Hi. Welcome to our NBA stats filing system. What would you like to do?\n")
    while(choice != 4):
        print("\nMAIN MENU:")
        print("1. Get stats")
        print("2. Create csv files")
        print("3. Sort Files")
        print("4. Quit\n")
        
        try:
            choice = int(input("What would you like to do? \n"))
        except ValueError:
            print("\n\nPlease Enter A Valid Number\n")
        if choice == 1:
            print("\nWhat kind of stats would you like? ")
            choice = nba_options()
            if choice == 4:
                choice = 0
            else:
                process_stats(choice)
        elif choice == 2:
            print("\nWhat kind of csv file do you want to create? ")
            choice = nba_options()
            if choice == 4:
                choice = 0
            else:
                process_csv_creation(choice)
        elif choice == 3:
            #we need to find out what we want to update
            print("")
            store_file()
        elif choice == 4:
            print("GODDBYE!")
        



if __name__ == "__main__":
    main()

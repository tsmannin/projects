from pathlib import Path
import nba.py as nba
import scrape.py as s

nba_2017_season = "https://www.basketball-reference.com/leagues/NBA_2017.html"
teams = {'boston celtics': 'BOS', 'cleveland cavaliers' : 'CLE', 'toronto raptors' : 'TOR',
        'washington wizards':'WAS', 'atlanta hawks':'ATL', 'milwaukee bucks':'MIL',
        'indiana pacers':'IND','chicago bulls':'CHI','miami heat':'MIA','detroit pistons':'DET',
        'charlotte hornets':'CHA','new york knicks': 'NYK','orlando magic': 'ORL', 'philadelphia 76ers':'PHI',
        'brooklyn nets':'BKN','golden state warriors':"GSW",'san antonio spurs':'SAS','houston rockets':'HOU',
        'los angeles clippers':'LAC', 'utah jazz': 'UTA', 'oklahoma city thunder':'OKC','memphis grizzlies':'MEM',
        'portland trail blazers':'POR', 'denver nuggets':'DEN', 'new orleans pelicans':'NOP', 'dallas mavericks':'DAL',
        'sacramento kings':'SAC', 'minnesota timberwolves':'MIn', 'los angeles lakers':'LAL','phoenix suns':'PHX'}

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

 #scrapes the data of a specific player
def scrape_player(url):
    matchObj = re.match(r'https://www.basketball-reference.com/players/b/(.*)02.html', url, re.M|re.I)
    if matchObj:
        html = urllib.urlopen(url)

        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table')

        header = []
        table_headers = table.find_all('thead')#we get the headers of each collumn
        for th in table_headers:
            t = th.find_all('th')
            header = [i.text for i in t]
        print(header)

        other = []
        advanced_List = []
        table_rows = table.find_all('tr')
        for tr in table_rows:
            a = tr.find_all('a')
            td = tr.find_all('td')
            advanced_List = [i.text for i in a]#makes a list containing dates
            if advanced_List and advanced_List[0] == '2016-17':#checks date
                other += [i.text for i in td]#inculdes it to our other list
        print(other)
    else:
        return []

def nba_options():
    print("1. Conference")
    print("2. Team")
    print("3. Player")
    print("4. Quit")
    choice = int(input())
    return choice


def process_stats(choice):
    if choice == 1:
        #print conference stats here
        conf = input("Enter conference name: (East/West)")
        s.scrape_conference(conf)
    elif choice == 2:
        #print team stats here
        team = input("Enter team name: ")
        url = build_team_url(team)
        s.scrape_team(url)
    elif choice == 3:
        #print player stats here
        player = input("Enter player name: (first name) (last name)")
        scrape_player(player)

    elif choice == 4:
        pass

def process_csv_creation(choice):
    if choice == 1:
        #create csv file for conference
        conf = input("Enter conference name: (East/West)")
        myConf = nba.Conference(conf, s.scrape_conference(conf))
    elif choice == 2:
        #create csv file for team
        team = input("Enter team name: ")
        url = build_team_url(team)
        myTeam = nba.Team(team, s.scrape_team(url))
    elif choice == 3:
        #create csv file for player
        player = input("Enter player name: (first name) (last name)")
        myPlayer = nba.Player(scrape_player(player))
        myPlayer.create_player_csv()
    elif choice == 4:
        pass

def store_file():
    savedir = Path(input("Enter the directory you want to save in."))
    if not savedir.exists():
        savedir.mkdir()

    file_name = input("What is the name of the file you want to store? (include the extension)")


def main():
    print("Hi. Welcome to our NBA stats filing system. What would you like to do?")
    print("1. Get stats")
    print("2. Create csv files")
    print("3. Sort Files")
    print("4. Quit")
    choice = int(input())
    if choice == 1:
        print("What kind of stats would you like?")
        choice = nba_options()
        process_stats(choice)
    elif choice == 2:
        print("What kind of csv file do you want to create?")
        choice = nba_options()
        process_csv_creation(choice)
    elif choice == 3:
        #we need to find out what we want to update
        print("")
        store_file()
    elif choice == 4:
        pass




if __name__ == "__main__":
    main()

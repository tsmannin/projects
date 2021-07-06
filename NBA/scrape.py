from bs4 import BeautifulSoup
from pathlib import Path
import nba as n
import urllib
import re
import string


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
    return "https://www.basketball-reference.com/teams/" + team + "/2017.html"

def build_player_url(name, team):
    url = build_team_url(team)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    tbody = soup.find_all('tbody')
    player_url = "https://www.basketball-reference.com"
    for t in tbody:
        tr = t.find_all('tr')
        for r in tr:
            a = r.find_all('a')
            if a[0].text == name:
                tag = a[0]['href']
                player_url += tag

    return player_url

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
        scrape_conference(conf)
    elif choice == 2:
        #print team stats here
        team = input("Enter team name: ")
        url = build_team_url(team)
        scrape_team(url, team)
    elif choice == 3:
        #print player stats here
        player = input("Enter player name: (first name) (last name)")
        first,last = player.split()
        url = build_player_url(first, last)
        list_of_stats = scrape_player(url, team)
        player = n.Player(list_of_stats)
        player.display()
    elif choice == 4:
        pass

def process_csv_creation(choice):
    if choice == 1:
        #create csv file for conference
        conf = input("Enter conference name: (East/West)")
        myConf = n.Conference(conf, scrape_conference(conf))
    elif choice == 2:
        #create csv file for team
        team = input("Enter team name: ")
        url = build_team_url(team)
        myTeam = n.Team(team, scrape_team(url, team))
        myTeam.create_team_csv(team)
    elif choice == 3:
        #create csv file for player
        player = input("Enter player's full name: ")
        team = input("Enter team name: ")
        url = build_team_url(team)
        url = build_player_url(player, team)
        myPlayer = n.Player(scrape_player(url, team))
        myPlayer.create_player_csv()
    elif choice == 4:
        pass

def store_file():
    savedir = Path(input("Enter the directory you want to save in."))
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
    elif choice == 2:
        team_path = savedir / Path("Teams")
        if not team_path.exists():
            team_path.mkdir()
        file = list(savedir.glob(file_name))
        move_to = team_path / Path(file_name)
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

def scrape_conference(conference):
    url = 'https://www.basketball-reference.com/leagues/NBA_2018.html'
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, 'lxml')

    header = []
    teams = []
    stats = []
    row = -1
    tabh = soup.find_all('thead')
    table = soup.find_all('tbody')
    for i,c in enumerate(tabh):
        conf = c.text.lower()

        if conf.find(conference) > 0 and i <= 2:#not case sensitive
            td = c.find_all('th')
            for f in td:
                header.append(f.text)
            row = i
    if row > 0:   #if we find the correct conference it will not be -1
        for i,c in enumerate(table):
            if i == row:
                tr = c.find_all('tr')
                a = c.find_all('a')
                for j in a:
                    teams.append([j.text])
                for f, c in enumerate(tr):
                    td = c.find_all('td')
                    stats.append([l.text for l in td])
                    stats[f].insert(0,teams[f][0])

    else:
        print("Sorry no conference Matching that name")
        return []
    stats.insert(0,header)
    return stats

def scrape_team(url, team):
    html = urllib.request.urlopen(url)
    matchObj = re.match(r'https://www.basketball-reference.com/teams/(.*)/2017.html', url, re.M|re.I)

    if matchObj:
        soup = BeautifulSoup(html, 'lxml')
        # header = []
        # tabh = soup.find_all('thead')
        # for tr in tabh:
        #     tr = tr.find_all('th')
        #     header += [i.text for i in tr]#looks for headers

        tbody = soup.find_all('tbody')
        stats = []
        roster = []
        for t in tbody:
            tr = t.find_all('tr')
            th = t.find_all('th')
            # for i in th:
            #     numbers.append([i.text])#numbers of all players
            # for i,c in enumerate(tr):
            #     td = c.find_all('td')
            #     roster.append([f.text for f in td])
            #     roster[i].insert(0,numbers[i][0])#inludes number of each player
            for r in tr:
               a = r.find_all('a')
               tag = a[0].text
               roster.append(tag)

        for player in roster:
            url = build_player_url(player, team)
            stat = scrape_player(url, team)
            header = stat[0]
            header.insert(0, "Name")
            stat = (stat[1])
            stat.insert(0, player)
            stats.append(stat)

        stats.insert(0,header)#includes headers to top of list
        return(stats)#returns a list of all players and headers
    else:
      return []

def scrape_player(url, team):
    matchObj = re.match(r'https://www.basketball-reference.com/players/(.*)/(.*).html', url, re.M|re.I)
    if matchObj:
        html = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table')

        header = []
        table_headers = table.find_all('thead')#we get the headers of each collumn
        for th in table_headers:
            t = th.find_all('th')
            header = [i.text for i in t]

        stats = []
        table_rows = table.find_all('tr')
        for tr in table_rows:
            a = tr.find_all('a')
            if len(a) > 2:
                if a[0].text == "2016-17":
                    if a[1].text == team:
                        td = tr.find_all('td')
                        stats.append([x.text for x in td])


        stats.insert(0,header)
        return stats
    else:
        return []

def scrape_conference(conference):
    url = 'https://www.basketball-reference.com/leagues/NBA_2017.html'
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, 'lxml')

    header = []
    teams = []
    stats = []
    row = -1
    tabh = soup.find_all('thead')
    table = soup.find_all('tbody')
    for i,c in enumerate(tabh):
        conf = c.text.lower()
        if conf.find(conference.lower()) > 0 and i <= 2:#not case sensitive
            td = c.find_all('th')
            for f in td:
                header.append(f.text)
            row = i
        break

    if row >= 0:   #if we find the correct conference it will not be -1
        for i,c in enumerate(table):
            if i == row:
                tr = c.find_all('tr')
                a = c.find_all('a')
                for j in a:
                    teams.append([j.text])
                for f, c in enumerate(tr):
                    td = c.find_all('td')
                    stats.append([l.text for l in td])
                    stats[f].insert(0,teams[f][0])
    else:
        print("Sorry no conference Matching that name")
        return []
    stats.insert(0,header)
    return stats




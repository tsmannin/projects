from bs4 import BeautifulSoup
import urllib
import pandas as pd
import csv

def basicStats():
    url = "https://www.basketball-reference.com/leagues/NBA_2017_totals.html    "
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, 'lxml')

    table = soup.find('table')

    basic_stats = []
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        basic_stats.append([i.text for i in td])

    return basic_stats
    #returns a list of the basic stats of all players


    # Each player has their own list with these stats
    # List format = Name(0), Pos(1), Age(2), Team(3), Games(4), Games Started(5), Minutes Played(6), Field Goals(7), Field Goal Attempts(8),
    # Field Goal Percentage(9), Three Pointers(10), Three Point Attempts(11), Three Point Percentage(12), Two Pointers(13), Two Point Attempts(14),
    # Two Point Percentage(15), Effective Field Goal Percentage(16), Free Throws(17), Free Throw Attempts(18), Free Throw Percentage(19),
    # Offensive Rebounds(20), Defensive Rebounds(21), Total Rebounds(22), Assists(23), Steals(24), Blocks(25), Turnovers(26),
    # Personal Fouls(27), Points(28)

def advancedStats():
    url = "https://www.basketball-reference.com/leagues/NBA_2017_advanced.html"
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, 'lxml')

    table = soup.find('table')

    advanced_stats = []
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        advanced_stats.append([i.text for i in td])

    return advanced_stats
    # returns a list of the advanced stats of all players

    # Each player has their own list with these stats
    # List format = Name(0), Pos(1), Age(2), Team(3), Games(4), Minutes Played(5), Player Efficiency Rating(6), True Shooting(7),
    # Three Point Attempt Rate(8), Free Throw Rate(9), ORB%(10), DRB%(11), TRB%(12), AST%(13), STL%(14), BLK%(15), TOV%(16), USG%(17),
    # OWS(18), DWS(19), WS(20), OBPM(21), DBPM(22), BPM(23), VORP(24)

def conferenceStandings():
    dfs = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2017_standings.html")
    conference = []
    for df in dfs:
        conference.append(df.values.tolist())#conference list

    return conference
    # returns a list of the conference standings

    # List format(each element is its own list as well) = List0[ Eastern Conference Teams(0-14) ]
    # List1[ Western Conference Teams(0-14) ]
    # List2[ "Atlantic Division"(0), Atlantic Teams(1-5), "Central Division"(6), Central Teamas(7-11), "SouthEast Division"(12), SouthEast Teams(13-17) ]
    # List3[ "NorthWest Division"(0), NorthWest Teams(1-5), "Pacific Division"(6), Pacific Teams(7-11), "SouthWest Division"(12), SouthWest Teams(13-17) ]

def main():
    #basicStats()
    #advancedStats()
    #conferenceStandings()


if __name__ == "__main__":
     main()
#you also need to run this on python2(in terminal type alias python=python2; confirm with python --version to check)

#i just need to find a way to find all the headers for every stat/conference or we can just organize them through
#our functions in the classes

# you need to install pandas to run this as well. Type 
# - "pip install pandas"
#       or
# - sudo apt-get install python-pandas
#       or
# - sudo easy_install pandas

# to install beautifulsoup
# -pip install bs4
#       or
# -sudo apt-get install python-bs4
#       or
# -sudo easy install bs4

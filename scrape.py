from bs4 import BeautifulSoup
import urllib
import pandas as pd
import csv

def scrape_team(url)
    html = urllib.urlopen(url)
    
    soup = BeautifulSoup(html, 'lxml')
    header = []
    tabh = soup.find_all('thead')
    for tr in tabh:
        tr = tr.find_all('th')
        header += [i.text for i in tr]#looks for headers
    
    tbody = soup.find_all('tbody')
    numbers = []
    roster = []
    for t in tbody:
        tr = t.find_all('tr')
        th = t.find_all('th')
        for i in th:
            numbers.append([i.text])#numbers of all players
        for i,c in enumerate(tr):
            td = c.find_all('td')
            roster.append([f.text for f in td])
            roster[i].insert(0,numbers[i][0])#inludes number of each player
            
    roster.insert(0,header)#includes headers to top of list
    return(roster)#returns a list of all players and headers




def scrape_player():
      url = "https://www.basketball-reference.com/leagues/NBA_2017_totals.html    "
    html = urllib.request.urlopen(url)
    
    soup = BeautifulSoup(html, 'lxml')
    
    table = soup.find('table')
    
    basic_stats = []
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')#looks through all <table data> tags to find data
        basic_stats.append([i.text for i in td])#gets text from table data 
     return basic_stats
    #returns a list of the basic stats of the players
def scrape_advanced_stats():
    url = "https://www.basketball-reference.com/leagues/NBA_2017_advanced.html"
    html = urllib.request.urlopen(url)
    
    soup = BeautifulSoup(html, 'lxml')
    
    table = soup.find('table')
    
    advanced_List = []
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td') #looks through all <table data> tags to find data
        advanced_List.append([i.text for i in td])#conference list
    return advanced_list

def scrape_conference():
    dfs = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2017.html")    
    
    conference = []
    for df in dfs:
        conference += df.values.tolist()#iterates through data frame to turn each line into list
     
    return conference
if __name__ == "__main__":
     main()
#you also need to run this on python2(in terminal type alias python=python2; confirm with python --version to check)

#i just need to find a way to find all the headers for every stat/conference or we can just organize them through
#our functions in the classes

# you need to install pandas to run this as well. Type 
- "pip install pandas"
      or
- sudo apt-get install python-pandas
      or
- sudo easy_install pandas

to install beautifulsoup
-pip install bs4
      or
-sudo apt-get install python-bs4
      or
-sudo easy install bs4

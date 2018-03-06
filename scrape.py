from bs4 import BeautifulSoup
import urllib
import pandas as pd
import csv
def main():
    
    url = "https://www.basketball-reference.com/leagues/NBA_2018_totals.html    "
    html = urllib.urlopen(url)
    
    soup = BeautifulSoup(html, 'lxml')
    
    table = soup.find('table')
    
    basic_stats = []
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        basic_stats.append([i.text for i in td])
    #returns a list of the basic stats of the players
    
    url = "https://www.basketball-reference.com/leagues/NBA_2018_advanced.html"
    html = urllib.urlopen(url)
    
    soup = BeautifulSoup(html, 'lxml')
    
    table = soup.find('table')
    
    advanced_List = []
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        advanced_List.append([i.text for i in td])#conference list
    
    
    
    dfs = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2018_standings.html")
    conference = []
    for df in dfs:
        conference.append(df.values.tolist())#conference list
    
if __name__ == "__main__":
     main()
#you also need to run this on python2(in terminal type alias python=python2; confirm with python --version to check)

#i just need to find a way to find all the headers for every stat/conference or we can just organize them through
#our functions in the classes

from bs4 import BeautifulSoup
import urllib
import pandas as pd
import csv
def scrape_player():
      url = "https://www.basketball-reference.com/leagues/NBA_2018_totals.html    "
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
def scrape_advanced_stas():
    url = "https://www.basketball-reference.com/leagues/NBA_2018_advanced.html"
    html = urllib.request.urlopen(url)
    
    soup = BeautifulSoup(html, 'lxml')
    
    table = soup.find('table')
    
    advanced_List = []
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td') #looks through all <table data> tags to find data
        advanced_List.append([i.text for i in td])#conference list
    return advanced_list

def scrape_confrence():
    dfs = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2018.html")    
    
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

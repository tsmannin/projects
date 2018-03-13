from bs4 import BeautifulSoup
import urllib
import re
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
    
def scrape_team(url):
    matchObj = False
    try: 
        matchObj = re.match(r'https://www.basketball-reference.com/teams/(.*)/2017.html', url, re.M|re.I)
    except TypeError:
        print("need string")
    if matchObj: 
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        header = []
        tabh = soup.find_all('thead')
        for tr in tabh:
            tr = tr.find_all('th')
            header += [i.text for i in tr]#looks for headers
        header.pop(6)
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
                roster[i].pop(6)
        roster.insert(0,header)#includes headers to top of list
        return(roster)#returns a list of all players and headers
    else:
        return []  
      
def scrape_player(url,year):
    matchObj = re.match(r'https://www.basketball-reference.com/players/(.*)/(.*).html', url, re.M|re.I)
    if matchObj:
        html = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table')
        name = soup.find()
        header = []
        table_headers = table.find_all('thead')#we get the headers of each collumn
        for th in table_headers:
            t = th.find_all('th')
            header = [i.text for i in t]
        

        other = []
        advanced_List = []
        table_rows = table.find_all('tr')
        for tr in table_rows:
            a = tr.find_all('a')
            td = tr.find_all('td')
            advanced_List = [i.text for i in a]#makes a list containing dates
            if advanced_List and advanced_List[0] == year:#checks date
                other.insert(0, advanced_List[0])
                other += [i.text for i in td]#inculdes it to our other list
        other.insert(0,header)
        return other
    else:
        return []

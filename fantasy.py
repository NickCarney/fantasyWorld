import requests, bs4

#list full of team abbreviations used by pro-football-ref
team_abvs = ['crd','atl','rav','buf','car','chi','cin','cle','dal','den','det','gbn','htx','clt','jax','kan','rai','sdg','ram','mia','min','nwe','nor','nyg','nyj','phi','pit','sfo','sea','tam','oti','was']

for team in team_abvs:
    url = 'https://www.pro-football-reference.com/teams/dal/2024.htm'

request = requests.get(url)
soup = bs4.BeautifulSoup(request.text, 'html.parser')
tables = soup.find_all('table')

print(len(tables))

for i in range(1,5):
    if i ==2:
        pass
    rows = tables[i].find_all('tr')
    for row in rows:
        deets = row.find_all('td')
        for deet in deets:
            print(deet.text, end=' ')
        print()
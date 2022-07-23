import requests
import pandas as pd
import bs4
import json
import datetime
from dateutil.parser import parse
from pandas.io.json import json_normalize

page = 0
leagues = ['EPL', 'La liga', 'Bundesliga', 'Serie A', 'Ligue 1']
match_ids = []
competition = []
seasons = []
date = 0

while True:
    if page > 18210:
        break
    base_url = 'https://understat.com/match/{}'
    url = base_url.format(page)
    res = requests.get(url)
    if 'The page you requested was not found' in str(res.text):
        page += 1
        continue
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    league = soup.find_all('li')[4].text
    if league not in leagues:
        page += 1
        continue
    match_date = parse(soup.find_all('li')[5].text)
    if match_date.month > 7:
        season = match_date.year
    else:
        season = (match_date.year) - 1
    match_ids.append(page)
    competition.append(league)
    seasons.append(season)
    page += 1

df = pd.DataFrame({'match_id':match_ids, 'competition':competition, 'year':seasons})

df.to_csv('Understat_match_ids.csv', index=False)

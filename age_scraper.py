import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = requests.get('https://basketball.realgm.com/nba/players/2022')
src = url.content
soup = bs(src, 'html.parser')

rows = soup.find_all('tr')

headers = rows[30]

col_headers = [td.get_text().replace('\n', '') for td in headers if td.get_text().replace('\n', '') != '']

final_df = pd.DataFrame(columns=col_headers)

players = rows[31:]

for player in players:
    player = [td.get_text().replace('\n', '') for td in player if td.get_text().replace('\n', '') != '']
    df = pd.DataFrame(player).transpose()
    df.columns = col_headers

    final_df = pd.concat([final_df, df], ignore_index=True)



final_df.to_csv('C:/Users/Schlenker18/Jupyter/50 Weeks 50 Projects/data/nba_player_age21-22.csv', index = False, sep = ',', encoding = 'utf-8')
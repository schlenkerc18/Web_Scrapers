import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import numpy as np

url = requests.get('https://www.sports-reference.com/cfb/years/2021-receiving.html')
src = url.content
soup = bs(src, 'html.parser')

rows = soup.find_all('tr')

print(rows[1])

headers = rows[1]

col_headers = [td.get_text().replace('\n', '') for td in headers if td.get_text().replace('\n', '') != '']

print(col_headers)

final_df = pd.DataFrame(columns=col_headers)

players = rows[2:]

for player in players:
    player = [td.get_text().replace('\n', '') for td in player if td.get_text().replace('\n', '') != '']
    df = pd.DataFrame(player).transpose()

    print(df)

    df.columns = col_headers

    final_df = pd.concat([final_df, df], ignore_index=True)

print(final_df)
#
# final_df.to_csv('C:/Users/Schlenker18/Jupyter/50 Weeks 50 Projects/data/wr_draft_position.csv',
#                 index = False, sep = ',', encoding = 'utf-8')
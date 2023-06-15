import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import numpy as np

url = requests.get('https://www.drafthistory.com/positions/wr.html')
src = url.content
soup = bs(src, 'html.parser')

rows = soup.find_all('tr')

headers = rows[1]

col_headers = [td.get_text().replace('\n', '') for td in headers if td.get_text().replace('\n', '') != '']

print(col_headers)

final_df = pd.DataFrame(columns=col_headers)

players = rows[2:]
year = ''  # placeholder variable

for player in players:
    player = [td.get_text().replace('\n', '') for td in player if td.get_text().replace('\n', '') != '']
    df = pd.DataFrame(player).transpose()
    df.columns = col_headers

    if (df.Year[0].strip() != ''):
        year = df.Year[0]
        # print('year:', year)
    else:
        # print('year:', year)
        df.Year = year
        # print("year is blank")

    final_df = pd.concat([final_df, df], ignore_index=True)

print(final_df)

final_df.to_csv('C:/Users/Schlenker18/Jupyter/50 Weeks 50 Projects/data/wr_draft_position.csv',
                index = False, sep = ',', encoding = 'utf-8')
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


url = requests.get('https://www.worldatlas.com/articles/mlb-teams-and-their-cities.html')
src = url.content
soup = bs(src, 'html.parser')

cities = soup.find_all('tr')

columns = [th.get_text().replace('\n', '') for th in cities[0]]
final_df = pd.DataFrame(columns=columns)

cities = cities[1:]

for city in cities:
    team = [td.get_text().replace('\n', '') for td in city.find_all('td')]

    temp_df = pd.DataFrame(team).transpose()
    temp_df.columns = columns

    # print(temp_df)
    final_df = pd.concat([final_df, temp_df], ignore_index=True)

final_df.to_csv('C:/Users/Schlenker18/Jupyter/50 Weeks 50 Projects/data/team_cities.csv', index = False, sep = ',', encoding = 'utf-8')

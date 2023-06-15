import requests
import json
import pandas as pd
import re
from bs4 import BeautifulSoup as bs



def scrape_salary(year):
    url = requests.get(f'https://www.spotrac.com/mlb/payroll/{year}/')
    src = url.content
    soup = bs(src, 'html.parser')

    team_info = soup.find_all('tr')

    columns = [th.get_text() for th in team_info[0].find_all('th')]
    final_df = pd.DataFrame(columns=columns)

    # remove table header row
    team_info = team_info[1:]

    for team in team_info:
        stats = [stat.get_text() for stat in team.find_all('td')]

        if (len(stats) != 10):
            league_avg = pd.DataFrame(stats).transpose()
            league_avg.insert(loc=0, column='Rank', value=15.5)
            league_avg.columns = columns
            continue

        df = pd.DataFrame(stats).transpose()
        df.columns = columns

        final_df = pd.concat([final_df, df], ignore_index=True)




    final_df = pd.concat([final_df, league_avg], ignore_index=True)

    csv_name = 'C:/Users/Schlenker18/Jupyter/50 Weeks 50 Projects/data/salary' + year + '.csv'
    final_df.to_csv(csv_name, index = False, sep = ',', encoding = 'utf-8')


years_to_scrape = ['2021']

for year in years_to_scrape:
    scrape_salary(year)



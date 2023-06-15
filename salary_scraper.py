import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_salaries(page):
    print('am i getting called')
    print(page)

    if page == 1:
        url = requests.get('http://www.espn.com/nba/salaries/_/year/2022')
    else:
        url = requests.get(f'http://www.espn.com/nba/salaries/_/year/2022/page/{str(page)}')

    print(url)
    src = url.content
    soup = bs(src, 'html.parser')

    player_table = soup.find_all('tr')

    columns = [td.get_text() for td in player_table[0]]
    players = player_table[1:]

    final_df = pd.DataFrame(columns = columns)

    for p in players:
        player = [td.get_text() for td in p]

        temp_df = pd.DataFrame(player).transpose()
        temp_df.columns = columns

        if temp_df.RK[0] != 'RK':
            final_df = pd.concat([final_df, temp_df], ignore_index = True)

    return final_df

if __name__ == "__main__":
    df = pd.DataFrame(columns = ['RK', 'NAME', 'TEAM', 'SALARY'])

    for i in range(1, 14):
        df = pd.concat([df, get_salaries(i)], ignore_index = True)

    df.to_csv('C:/Users/Schlenker18/Jupyter/50 Weeks 50 Projects/data/nba_salaries21-22.csv', index = False, sep = ',', encoding = 'utf-8')
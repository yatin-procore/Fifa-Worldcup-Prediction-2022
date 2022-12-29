import pandas as pd
import requests
from bs4 import BeautifulSoup

years = [1930, 1934, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 2002, 2006, 2010, 2014, 2018]


# getting list of matches by years od worldcup
def get_matches(year):
    # Connecting to website to collect data from the desires year of worldcup

    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    # starting to webscrape the website

    # collecting the list od all matches in the worldcup and looping through it to get results of all the matches
    matches = soup.find_all('div', class_='footballbox')

    # creating list for better usecase
    home = []
    scores = []
    away = []

    # creating a for loop to go through each interested element and appending them to the list created above
    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        scores.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    # creating dictionary to organize the data
    dict_football = {'Home Team': home, 'Match Scores': scores, 'Away Team': away}
    # creating a data frame and returning the results gathered back to dataframe
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football


# extracting data for all the yers of worldcup

# fifa = []
# for year in years:
#   fifa.append(get_matches(year))

# here we are converting the above commented for loop code into list comprehensions and get each dataframe per year
fifa = [get_matches(year) for year in years]

# printing the list of matches gathered using the above comprehensive list
# print(fifa)

# concatenating the results/tables of all the worldcup
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index=False)



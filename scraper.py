from msilib.schema import ODBCDataSource
from bs4 import BeautifulSoup

import pandas as pd
import requests

def main():
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    url = "https://www.covers.com/sport/football/ncaaf/odds"
    results = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(results.text, "html.parser")
    openOddsMoneyLine = parseMoneyLineOpenOdds(soup)
    # print(openOddsMoneyLine)

def parseMoneyLineOpenOdds(soup):
    tableOdds = soup.find_all('table')[0] #odds
    games_odds = tableOdds.find_all('div', '__openOdds')
    teams_odds = tableOdds.find_all('div', '__teams')
    

    d = {'Home Team'}
    openOdds = pd.DataFrame(data=d)
 
    for game_odds, team_odds in zip(games_odds, teams_odds):
        away = team_odds.find('div', '__away')
        awayImg = away.find('a')
        awayTeam = awayImg.find('img')['title']

        home = team_odds.find('div', '__home')
        homeImg = home.find('a')
        homeTeam = homeImg.find('img')['title']

        awayOdds = game_odds.find('div', '__awayOdds')
        away_american = awayOdds.find('div', 'American __american').string
        away_decimal = awayOdds.find('div', 'Decimal __decimal').string
        away_Fraction = awayOdds.find('div', '__fractional').string

        homeOdds = game_odds.find('div', '__homeOdds')
        home_american = homeOdds.find('div', 'American __american').string
        home_decimal = homeOdds.find('div', 'Decimal __decimal').string
        home_Fraction = homeOdds.find('div', 'Fraction __fractional').string
        
        print(awayTeam + " " + away_american + " " + away_decimal + " " + away_Fraction)
        print(homeTeam + " " + home_american + " " + home_decimal + " " + home_Fraction)
          
        openOdds.loc[len(openOdds.index)] = {homeTeam: {home_american, home_decimal, home_Fraction}, 
                                            awayTeam: {away_american, away_decimal, away_Fraction}}
    
    return(openOdds)

if __name__ == "__main__":
    main()
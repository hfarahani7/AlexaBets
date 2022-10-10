from bs4 import BeautifulSoup

import pandas as pd

def main():
    sport = "ncaaf/odds"
    url = getUrl(sport)

    soup = BeautifulSoup(url, "html.parser")
    df = parse_soup(soup)

    #add query functions here

def getUrl(sport):
    return("https://www.covers.com/sport/football/ncaaf/odds")

def parse_soup(soup):
    #create dataframe w/ all data

    #div classes needed
    #tr class="oddsGameRow" 
        # data-home-conference="American Athletic"
        # data-away-conference="American Athletic"
        # data-home-team-rank="-1"
        # data-away-team-rank="-1"
        #div class="__startDate"
            #div class="__date"
            #div class="__time"
        #div 

    #where are team names?

    oddsGameRows = soup.find_all("tr class=\"oddsGameRow\"")
    for oddsGameRow in oddsGameRows:
        home_conf = oddsGameRow['data-home-conference']
        home_rank = oddsGameRow['data-home-team-rank']
        away_conf = oddsGameRow['data-away-conference']
        away_rank = oddsGameRow['data-away-team-rank']

        descendents = oddsGameRow.descendents
        date = descendents.find("__date")
        time = descendents.find("__time")

        #df.addrow(all this stuff)

    #tr class="covers-CoversOdds-mainTR oddsGameRow"
        # data-home-conference="American Athletic"
        # data-away-conference="American Athletic"
        # data-home-team-rank="-1"
        # data-away-team-rank="-1"
        #td class=covers-CoversMatchups-centerAlignHelper covers-CoversOdss-oddsTd covers-CoversOdds-odssTdSpecial liveOddsCell __awaiting
            #data-book="PointsBet"
            #data-game="266024"
            #data-type="spread"
            #data-date="1664921635"
            #div class="__bookOdds covers-Covers-Odds-withNoBorder"
                #div class="__awayOdds covers-CoversMatchups-topOddsAway"
                #div class="__homeOdds  "
                    #div class="American __american"
        
    pass

if __name__ == "__main__":
    main()
"""
__author__: Shivank Batra(@prstrggr)

A Python module to scrape football shots data from understat.com.

"""
#import required packages
import pandas as pd
from selenium import webdriver
import json
import bs4
from pandas.io.json import json_normalize

class Understat:
    """
    contains methods to scrape data from understat.com for either a single game or a whole season.
    """

    def __init__(self, base_url='https://understat.com/match/{}'):
        """
        Function to initialize the object of the class.

        Args:
        base_url (str): common url for all the games available on understat.com. Defaults to "https://understat.com/match/{}"
        """
        self.base_url = base_url
        self.chrome_driver_path = r'C:\Users\shivank\Desktop\New folder\selenium\chromedriver.exe'


    def single_match(self, page):
        """
        Function to scrape data for a single game
        Args:
        base_url (string): url of the understat.com website from where the data has to be scraped.
        page (int): match id of the game for which the user wants the shots data.
        """
        url = self.base_url.format(page)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=options)
        driver.get(url)
        soup = bs4.BeautifulSoup(driver.page_source)
        scripts = soup.find_all('script')
        strings = str(scripts[3])
        ind_start = strings.index("('")+2
        ind_end = strings.index("')")
        json_data = strings[ind_start:ind_end]
        json_data = json_data.encode('utf8').decode('unicode escape')
        data = json.loads(json_data)
        home_df = json_normalize(data['h'],sep='_')
        away_df = json_normalize(data['a'],sep='_')
        combined = pd.concat([home_df, away_df])
        driver.close()
        return combined


    def season(self, league, year, team=None, player=None):
        """
        Function to scrape data for a whole season for a particular league.

        Args:
        league (str): League for which the user wants the data.
        year (int): Season for which the user wants the data. [inputting 15 will return the data for the season 15/16]
        team (str): Team for which the user wants the data. Defaults to None.
        player(str): Player for which the user wants the data. Defaults to None.
        """
        #creating a dataframe from a csv file containing all the match_ids, competition and season info for all the games available on understat.com.
        #Used as a reference point to filter the dataframe for the specified user input.
        df = pd.read_csv('Understat_match_ids.csv')
        df = df[(df['competition'] == league) & (df['year'] == year)]
        match_ids = df['match_id'].tolist()
        final_df = pd.DataFrame()
        understat = Understat()

        for match_id in match_ids:
            combined = understat.single_match(match_id)
            final_df = pd.concat([final_df, combined])

        if team != None:
            final_df = final_df[(final_df['h_team'] == team) | (final_df['a_team'] == team)]

        if player != None:
            final_df = final_df[final_df['player'] == player]

        return final_df

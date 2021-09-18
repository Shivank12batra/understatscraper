# understatscraper

A Python package to scrape shots data from understat.com for either a single game or a whole season.

Author: Shivank Batra(@prstrggr)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install understatscraper.

```bash
pip install understatscraper
```

## Usage
### Scraping Data For A Single Game
You can get shots data for a single game by calling the single_match() method of the Understat class.

The function takes one single parameter which is the match id(int) of the game. Match id of the game can be found in the [url](https://understat.com/match/16414) at the end. Here we have taken the example of Liverpool-Leeds game:

```python
from understatscraper import Understat

# creating an instance of the class Understat
understat = Understat()

#Calling the function to scrape data for a specific game id 16414
#returns a dataframe containing all the shots data from the game
df = understat.single_match(16414)
print(df)
```
### Scraping Data For A Whole Season
You can get shots data for a whole season and for a specified league by calling the season() method of the Understat class.

It takes four parameters:

1. league(str)
2. year(int)
3. team(str). Default value as None.
4. player(str). Default value as None.

NOTE:

1. Before calling the season function, make sure to download this [csv](https://drive.google.com/file/d/1_DamxA2SaJpxfmCZv9lJ-7uDgeW0RDOj/view?usp=sharing) file since it will used as a reference point to easily loop over the match ids according to the specified user input when calling the function.

2. If you want the data for let's say 20/21 season then input the preceding year i.e. 2020 as the year parameter to get the data for 20/21 season.

3. Data is available from the 2014 -2015 to 2021-2022 season.

4. Data for the 2021-2022 is only available till Gameweek 4.

5. Data is only available for five leagues:
   1. EPL
   2. La liga
   3. Ligue 1
   4. Bundesliga
   5. Serie A

6. Input 'La liga' as the league parameter with a smaller case l in liga when wanting the data for LaLiga. Similarly, for Premier league, input 'EPL'.

```python
from understatscraper import Understat

# creating an instance of the class Understat
understat = Understat()

#calling a function to scrape shots data for the EPL season 20/21
#returns a dataframe containing all the shots data from the EPL season 20/21
df = understat.season('EPL', 2020)
print(df)

#calling a function to scrape shots data for Raheem Sterling from the 20/21 EPL season.
df = understat.season('EPL', 2020, team='Manchester City', player='Raheem Sterling')
print(df)
```
NOTE:

While inputting the team and player, make sure to input exact team and player name that is available on [understat.com](https://understat.com/)


## Contributing
For any doubts or suggestions you can contact me [here](https://twitter.com/prstrggr?lang=en)

## License
[MIT](https://choosealicense.com/licenses/mit/)

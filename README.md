# MLB/NBA/NHL head to head record visualizations  
  
Plot the head to head history between two teams in the MLB, NBA, or NHL. An extension of my previous MLB head to head record visualization driver.  
  
## How To  
  
* Go to the ```driver``` folder  
* Run it using: ```python3 h2hviz.py mlb|nba|nhl [-ohap] TEAM1 TEAM2```  
* A list of team nicknames and their associated teams:  
  
MLB:  
```json
{
	"ari": "Arizona Diamondbacks",
	"atl": "Atlanta Braves",
	"bal": "Baltimore Orioles",
	"bos": "Boston Red Sox",
	"chi": "Chicago Cubs",
	"wsx": "Chicago White Sox",
	"cin": "Cincinnati Reds",
	"cle": "Cleveland Indians",
	"col": "Colorado Rockies",
	"det": "Detroit Tigers",
	"hou": "Houston Astros",
	"kc": "Kansas City Royals",
	"laa": "Los Angeles Angels",
	"la": "Los Angeles Dodgers",
	"mia": "Miami Marlins",
	"mil": "Milwaukee Brewers",
	"min": "Minnesota Twins",
	"nym": "New York Mets",
	"nyy": "New York Yankees",
	"oak": "Oakland Athletics",
	"phi": "Philadelphia Phillies",
	"pit": "Pittsburgh Pirates",
	"sd": "San Diego Padres",
	"sf": "San Francisco Giants",
	"sea": "Seattle Mariners",
	"stl": "St. Louis Cardinals",
	"tb": "Tampa Bay Rays",
	"tex": "Texas Rangers",
	"tor": "Toronto Blue Jays",
	"wsh": "Washington Nationals"
}
```
  
NBA:  
```json
{
	"atl": "Atlanta Hawks",
	"bos": "Boston Celtics",
	"brk": "Brooklyn Nets",
	"cha": "Charlotte Hornets",
	"chi": "Chicago Bulls",
	"cle": "Cleveland Cavaliers",
	"dal": "Dallas Mavericks",
	"den": "Denver Nuggets",
	"det": "Detroit Pistons",
	"gs": "Golden State Warriors",
	"hou": "Houston Rockets",
	"ind": "Indiana Pacers",
	"lac": "Los Angeles Clippers",
	"lal": "Los Angeles Lakers",
	"mem": "Memphis Grizzlies",
	"mia": "Miami Heat",
	"mil": "Milwaukee Bucks",
	"min": "Minnesota Timberwolves",
	"no": "New Orleans Pelicans",
	"ny": "New York Knicks",
	"okc": "Oklahoma City Thunder",
	"orl": "Orlando Magic",
	"phi": "Philadelphia 76ers",
	"phx": "Phoenix Suns",
	"por": "Portland Trail Blazers",
	"sac": "Sacramento Kings",
	"sa": "San Antonio Spurs",
	"tor": "Toronto Raptors",
	"uth": "Utah Jazz",
	"wsh": "Washington Wizards"
}
```
  
NHL:  
```json
{
	"ana": "Anaheim Ducks",
	"ari": "Arizona Coyotes",
	"bos": "Boston Bruins",
	"buf": "Buffalo Sabres",
	"cal": "Calgary Flames",
	"car": "Carolina Hurricanes",
	"chi": "Chicago Blackhawks",
	"col": "Colorado Avalanche",
	"clb": "Columbus Blue Jackets",
	"dal": "Dallas Stars",
	"det": "Detroit Red Wings",
	"edm": "Edmonton Oilers",
	"fla": "Florida Panthers",
	"la": "Los Angeles Kings",
	"min": "Minnesota Wild",
	"mon": "Montreal Canadiens",
	"nsh": "Nashville Predators",
	"nj": "New Jersey Devils",
	"nyi": "New York Islanders",
	"nyr": "New York Rangers",
	"otw": "Ottawa Senators",
	"phi": "Philadelphia Flyers",
	"pit": "Pittsburgh Penguins",
	"sj": "San Jose Sharks",
	"stl": "St. Louis Blues",
	"tb": "Tampa Bay Lightning",
	"tor": "Toronto Maple Leafs",
	"van": "Vancouver Canucks",
	"vgk": "Vegas Golden Knights",
	"wsh": "Washington Capitals",
	"win": "Winnipeg Jets"
}
```
  
* Flags:  
	* -o: overall win percentage  
	* -h: home win percentage  
	* -a: away win percentage  
	* -p: playoff win percentage  

* Instructions for using virtualenv:  
	* If you do not have virtual environments set up in Python, run: ```pip3 install virtualenv```  
	* To activate the virtual environment, run: ```source h2env/bin/activate```  
	* Install the packages: ```pip3 install -r requirements.txt```  
	* Follow the instructions as above to run the visualization driver  
	* To exit the virtual environment, run: ```deactivate```  
    
## Extra Notes  
  
* Postseason games are included in the visualization data  
* Gap years are filled in with the last valid year's data. So if there were no games played between Team A and Team B between 2015 and 2017, then the years 2015-2017 would be filled with 2014's respective data on the graph, but would not factor into calculations for future years  
* Tie games do not count as a win nor a loss in the calculations  
  
## The Dilemma of the Vegas Golden Knights  
They were formed in 2017, so they only have one season of data. For the sake of completion, I have included them, but give it some time before the data becomes truly relevant  
  
## Why No NFL Visualizations?  
   
The main reason is that the sample size of most head to head records is too small, sitting at around 10-15 games (due to the NFL regular season consisting of only 16 games per team). Thus, visualizations will not be as useful. Additionally, I don't like the NFL and the culture surrounding it, so please refrain from asking me to include it. You could call me religiously opposed to the NFL; totally fine by me.  
  
## Credit  
  
All data was gathered from mcubed.net.  
  
## Next Update  
  
Coming soon  
  
## Contact  
  
Let me know what you think or any suggestions you're willing to give at alexfromdavis@gmail.com.
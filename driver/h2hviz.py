import sys
sys.path.insert(0, '../globals')

import re
import json
import importlib
import mlbinfo
import nbainfo
import nhlinfo
import miscinfo
import parser
import matplotlib.pyplot as plt
import matplotlib.ticker
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

# Check if the league is valid
def validate_league():
	league = None

	if sys.argv[0] not in miscinfo.good_leagues:
		print('ERROR: invalid league specified. Please consult the README to see acceptable leagues.')
		sys.exit(1)

	league = sys.argv[0]
	sys.argv.remove(sys.argv[0])

	return league



# Make sure all flags specified are valid
def extract_flags():
	flags = []

	while (sys.argv[0][0] == '-'):
		if len(sys.argv[0]) == 1:
			print('ERROR: empty flag specified. Please consult the README for acceptable flags.')
			sys.exit(1)

		for char in sys.argv[0][1:]:
			adj_flag = char.lower()

			if adj_flag not in miscinfo.good_flags:
				print('ERROR: invalid flag specified: -%s. Please consult the README for acceptable flags.' % adj_flag)
				sys.exit(1)
			elif adj_flag in flags:
				print('ERROR: duplicate flag specified: -%s' % adj_flag)
				sys.exit(1)

			flags.append(adj_flag)
		
		sys.argv.remove(sys.argv[0])

	if len(flags) == 0:
		flags = miscinfo.good_flags

	return flags



# Check if two teams exist and are not equal
def validate_teams(league):
	fav = sys.argv[0]
	opp = sys.argv[1]

	names = mlbinfo.full_names if league == 'mlb' else (nbainfo.full_names if league == 'nba' else nhlinfo.full_names)	

	if fav not in names or opp not in names:
		print('ERROR: one or both of the teams you specified is invalid. Please consult the README for acceptable abbreviations based on the league you entered.')
		sys.exit(1)

	if fav == opp:
		print('ERROR: You cannot specify the same team twice')
		sys.exit(1)

	return (fav, opp)



def visualize(win_perc_data, flags, fav, opp, scraper):
	x = [*win_perc_data]

	y_overall = [win_perc_data[val]['overall_win_percentage'] for val in [*win_perc_data]]
	y_home = [win_perc_data[val]['home_win_percentage'] for val in [*win_perc_data]]
	y_away = [win_perc_data[val]['away_win_percentage'] for val in [*win_perc_data]]
	y_playoff = [win_perc_data[val]['playoff_win_percentage'] for val in [*win_perc_data]]

	if 'o' in flags:
		plt.plot(x, y_overall, 'ro', label='Overall winning percentage')
	if 'h' in flags:
		plt.plot(x, y_home, 'go', label='Home winning percentage')
	if 'a' in flags:
		plt.plot(x, y_away, 'bo', label='Away winning percentage')
	if 'p' in flags:
		plt.plot(x, y_playoff, 'mo', label='Playoff winning percentage')

	fav_name = mlbinfo.full_names[fav] if scraper.league == 'mlb' else (nbainfo.full_names[fav] if scraper.league == 'nba' else nhlinfo.full_names[fav])
	opp_name = mlbinfo.full_names[opp] if scraper.league == 'mlb' else (nbainfo.full_names[opp] if scraper.league == 'nba' else nhlinfo.full_names[opp])

	plt.title('%s vs %s' % (fav_name, opp_name))

	plt.xlabel('Year')
	plt.ylabel('Win percentage')

	plt.legend(loc='upper right')

	plt.axis([min(x) - 1, max(x) + 1, 0, 100.0])

	locator_x = matplotlib.ticker.MultipleLocator(1)
	plt.gca().xaxis.set_major_locator(locator_x)

	locator_y = matplotlib.ticker.MultipleLocator(10)
	plt.gca().yaxis.set_major_locator(locator_y)

	plt.show()




def main():
	if len(sys.argv) < 4 or len(sys.argv) > 8:
		print('USAGE: python3 h2hviz.py [-ohap] LEAGUE TEAM1 TEAM2')
		sys.exit(1)

	sys.argv.remove(sys.argv[0])

	league = validate_league()
	flags = extract_flags()
	fav, opp = validate_teams(league)

	scraper = parser.H2HViz(league, fav, opp, flags)
	win_perc_data = scraper.search_data()

	with open('cum_win.json', 'w') as outfile:
		outfile.write(json.dumps(win_perc_data, indent=4))

	visualize(win_perc_data, flags, fav, opp, scraper)

if __name__ == '__main__':
	main()
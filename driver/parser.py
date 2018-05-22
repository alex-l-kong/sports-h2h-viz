import sys
sys.path.insert(0, '../globals')

import mlbinfo
import nbainfo
import nhlinfo
import miscinfo
import re
import json
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import urlopen

class H2HViz:
	def __init__(self, league, fav, opp, flags=['o', 'h', 'a', 'p']):
		self.league = league
		self.fav = fav
		self.opp = opp
		self.flags = flags
		self.url = 'http://mcubed.net/%s/%s/%s.shtml' % (league, fav, opp)
		self.elems = BeautifulSoup(urlopen(self.url), 'lxml').findAll('span', {'class': 'hovl'})

	def fetch_elems(self, bsobj):
		all_h2h_data = bsobj.findAll('span', {'class': 'hovl'})
		trimmed_data = [x for x in all_h2h_data if re.match(r'\d\d\d\d:', x)]

	def fill_gaps(self, stats, year, last_year):
		if year - last_year > 1:
			for gap in range(last_year + 1, year):
				stats[gap] = stats[last_year].copy()
				stats[gap]['gap_year'] = True

		return stats

	def add_nhl(self, data, stats):
		add_on = {}
		scores = data[0]

		year = int(scores[0])
		last_year = [*stats][len(stats) - 1] if len(stats) > 0 else year # to prevent len(stats) - 1 from equalling -1
		stats = self.fill_gaps(stats, year, last_year)

		add_on['overall_wins'] = int(scores[1])
		add_on['overall_losses'] = int(scores[2])
		add_on['overall_ties'] = int(scores[3])
		add_on['home_wins'] = int(scores[4])
		add_on['home_losses'] = int(scores[5])
		add_on['home_ties'] = int(scores[6])
		add_on['away_wins'] = int(scores[7])
		add_on['away_losses'] = int(scores[8])
		add_on['away_ties'] = int(scores[9])
		add_on['playoff_wins'] = int(scores[10])
		add_on['playoff_losses'] = int(scores[11])
		add_on['gap_year'] = False
		# there are no ties in the playoffs, so that last column doesn't matter, it's just there for formalities

		stats[year] = add_on
		return stats

	def add_mlbnba(self, data, stats):
		add_on = {}
		scores = data[0]

		year = int(scores[0])
		last_year = [*stats][len(stats) - 1] if len(stats) > 0 else year # to prevent len(stats) - 1 from equalling -1
		stats = self.fill_gaps(stats, year, last_year)

		add_on['overall_wins'] = int(scores[1])
		add_on['overall_losses'] = int(scores[2])
		add_on['home_wins'] = int(scores[3])
		add_on['home_losses'] = int(scores[4])
		add_on['away_wins'] = int(scores[5])
		add_on['away_losses'] = int(scores[6])
		add_on['playoff_wins'] = int(scores[7])
		add_on['playoff_losses'] = int(scores[8])
		add_on['gap_year'] = False

		stats[year] = add_on
		return stats

	def tally_percs(self, stats):
		win_percs = {}

		total_wins = 0
		total_losses = 0
		total_home_wins = 0
		total_home_losses = 0
		total_away_wins = 0
		total_away_losses = 0
		total_playoff_wins = 0
		total_playoff_losses = 0
		
		for key in stats:
			# if it is not a gap year then update the corresponding information
			# otherwise, just copy the data from previous year's entry
			if stats[key]['gap_year'] == False:
				total_wins += stats[key]['overall_wins']
				total_losses += stats[key]['overall_losses']
				total_home_wins += stats[key]['home_wins']
				total_home_losses += stats[key]['home_losses']
				total_away_wins += stats[key]['away_wins']
				total_away_losses += stats[key]['away_losses']
				total_playoff_wins += stats[key]['playoff_wins']
				total_playoff_losses += stats[key]['playoff_losses']

				# a special case because teams don't see each other every year
				# so many records will be 0-0, and we don't want to divide by 0
				overall_win_percentage = total_wins / (total_wins + total_losses) * 100 # this one will never be 0-0 though
				home_win_percentage = 0 if (total_home_wins == 0 and total_home_losses == 0) else (total_home_wins / (total_home_wins + total_home_losses) * 100)
				away_win_percentage = 0 if (total_away_wins == 0 and total_away_losses == 0) else (total_away_wins / (total_away_wins + total_away_losses) * 100)
				playoff_win_percentage = 0 if (total_playoff_wins == 0 and total_playoff_losses == 0) else (total_playoff_wins / (total_playoff_wins + total_playoff_losses) * 100)

				win_percs[key] = {'overall_win_percentage': overall_win_percentage,
						 	 	  'home_win_percentage': home_win_percentage,
						 	 	  'away_win_percentage': away_win_percentage,
						 	 	  'playoff_win_percentage': playoff_win_percentage}
			else:
				win_percs[key] = win_percs[key - 1]

		return win_percs

	# def cum_win_nhl(self, stats):
	# 	win_percs = {}

	# 	overall_earned = 0
	# 	overall_poss = 0
	# 	home_earned = 0
	# 	home_poss = 0
	# 	away_earned = 0
	# 	away_poss = 0
	# 	total_playoff_wins = 0
	# 	total_playoff_losses = 0

	# 	for key in stats:
	# 		if stats[key]['gap_year'] == False:
	# 			overall_earned += stats[key]['overall_wins'] * 2 + stats[key]['overall_ties']
	# 			overall_poss += (stats[key]['overall_wins'] + stats[key]['overall_ties'] + stats[key]['overall_losses']) * 2
	# 			home_earned += stats[key]['home_wins'] * 2 + stats[key]['home_ties']
	# 			home_poss += (stats[key]['home_wins'] + stats[key]['home_ties'] + stats[key]['home_losses']) * 2
	# 			away_earned += stats[key]['away_wins'] * 2 + stats[key]['away_ties']
	# 			away_poss += (stats[key]['away_wins'] + stats[key]['away_ties'] + stats[key]['away_losses']) * 2
	# 			total_playoff_wins += stats[key]['playoff_wins']
	# 			total_playoff_losses += stats[key]['playoff_losses']
	# 		else:
	# 			win_percs[key] = win_percs[key - 1]

	# Pull the specified head to head record and process it
	def search_data(self):
		stats = {}

		for index, elem in reversed(list(enumerate(self.elems))):
			# this is because the NHL had tie games pre-2004-05 lockout, so an extra column keeps track of tie games (which earned each team 1 point)
			nhl_re = r' (\d\d\d\d):\s+(\d+)-(\d+)-(\d+)[\.\s\d]+ \| \s+(\d+)-(\d+)-(\d+)[\.\s\d]+ \| \s+(\d+)-(\d+)-(\d+)[\.\s\d]+ \| \s+(\d+)-(\d+)-(\d+)[\.\s\d]+'
			mlbnba_re = r' (\d\d\d\d):\s+(\d+)-(\d+)[\.\s\d]+ \| \s+(\d+)-(\d+)[\.\s\d]+ \| \s+(\d+)-(\d+)[\.\s\d]+ \| \s+(\d+)-(\d+)[\.\s\d]+'
			data = re.findall(nhl_re, elem.text) if self.league == 'nhl' else re.findall(mlbnba_re, elem.text)

			if len(data) > 0:
				stats = self.add_nhl(data, stats) if self.league == 'nhl' else self.add_mlbnba(data, stats)

		return self.tally_percs(stats)
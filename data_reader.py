import csv
from collections import defaultdict

d = defaultdict(int)


def win_scores(a, b):
    '''prints out the number of weighted games won among 2 teams'''
    print(d[f'{a}:{b}'], d[f'{b}:{a}'])


def weighted_score(a, b):
    '''prints the weighted chance of winning among 2 teams'''
    print(score_dict[f'{a}:{b}'])


with open('results.csv', 'r', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        year, month, day = row['date'].split('-')
        time_passed = int(year) - 1872
        weight = 0.05
        score = weight * time_passed
        if row['home_score'] > row['away_score']:
            d[f'{row["home_team"]}:{row["away_team"]}'] += score
        elif row['home_score'] < row['away_score']:
            d[f'{row["away_team"]}:{row["home_team"]}'] += score


score_dict = defaultdict(int)
match_pairs = list(d.keys())

for key in match_pairs:
    winner, loser = key.split(':')
    score_dict[f'{winner}:{loser}'] = d[f'{winner}:{loser}'] - d[f'{loser}:{winner}']

# Python 3.11.5
import math

file = open("Results.txt", "r", encoding="utf-8")
results = file.readlines()
games = [[]]
interesting_people = ["Юля","Оля"]
for line in results:
    if line.strip() != 'STOP':
        games[-1].append(line.strip().split())
    else:
        games.append([])
for game in games:
    print(game)
def receive(game):
    n = len(game)
    k=len(game[0]) - 1
    results = [None] * k
    for i in range(k):
        results[i]=[]
        for j in range(n):
            results[i].append((game[j][0], float(game[j][i + 1])))
    return n, k, results



def expected_score(rating_own, rating_opponents):
    """
    Computes the expected score for a single player against multiple opponents.
    """
    return sum(1 / (1 + 10 ** ((rating - rating_own) / 400)) for rating in rating_opponents) / (len(rating_opponents))


def update_elo_ratings(player_ratings, player_scores, total_points=100, K=300):
    """
    Updates the ratings of players based on their scores in a single game.

    player_ratings: dict with player names as keys and their ratings as values.
    player_scores: dict with player names as keys and their game scores as values.
    total_points: total points distributed among players in the game.
    K: adjusting factor, typically varies between 10 and 40.
    """
    num_players = len(player_ratings)

    new_ratings = {}
    for player in player_ratings:
        rating_own = player_ratings[player]
        opponents = [player_ratings[p] for p in player_ratings if p != player]
        expected = expected_score(rating_own, opponents)
        actual = player_scores[player]*num_players/2 / total_points

        new_rating = rating_own + K * (actual - expected)
        new_ratings[player] = new_rating

    return new_ratings

def calc(n,k,results):
    rezi = {}
    for i in range(k):
        s=0
        slov={}
        for j in range(n):
            imya,rez = results[i][j]
            rez=float(rez)
            s+=rez
            slov[imya]=rez
        for imya in slov:
            slov[imya]=slov[imya]/s
            if imya in rezi:
                rezi[imya]+=slov[imya]*100
            else:
                rezi[imya]=slov[imya]*100

    return rezi
def rat(x):
    if x not in rate:
        return 1500
    return rate[x]

def print_sorted_dict_by_value(input_dict):
    # Сортируем словарь по значениям
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)

    for key, value in sorted_items:
        print(f"{key}: {round(value)}")

rate = dict()
for game in games:
    #print(game)
    n,k,results=receive(game)
    rez=calc(n,k,results)
    print(rez)
    rates = dict()
    #print(rez)
    for i in rez:
        if i in rate:
            rates[i] = rate[i]
        else:
            rates[i] = 1500
    new_ratings = update_elo_ratings(rates, rez, 100 * k)
   # print(new_ratings)
    rate.update(new_ratings)
    #print(rate)
    #print("AAA", max(rate.values()))
print_sorted_dict_by_value(rate)
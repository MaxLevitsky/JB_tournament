# Python 3.11.5
import math


start_rate = 1500

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
        return start_rate
    return rate[x]

def print_sorted_dict_by_value(input_dict):
    # Сортируем словарь по значениям
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)

    for key, value in sorted_items:
        print(f"{key}: {round(value)}")


def print_report(player,report):
    rep = report[player]
    print(f"игрок {player}:")
    r = start_rate
    for res in rep:
        print(f"поменял(-a) рейтинг с {round(r,1)} на {round(res[0],1)}, играя против {res[1]} соперников(дельта {round(res[0] - r,1)})")
        r = res[0]

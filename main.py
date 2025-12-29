from game_calculation import receive, calc, start_rate, update_elo_ratings, print_sorted_dict_by_value, print_report

file = open("Results.txt", "r", encoding="utf-8")
results = file.readlines()
games = [[]]
interesting_people = ["Юля","Оля","Уля","Даша"]
for line in results:
    if line.strip() != 'STOP':
        games[-1].append(line.strip().split())
    else:
        games.append([])
for game in games:
    print(game)
rate = dict()
report = dict()
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
            rates[i] = start_rate
    new_ratings = update_elo_ratings(rates, rez, 100 * k)
    for player in rez:
        if player not in report:
            report[player] = [(new_ratings[player],len(rez)-1)]
        else:
            report[player].append((new_ratings[player],len(rez)-1))
   # print(new_ratings)
    rate.update(new_ratings)
    #print(rate)
    #print("AAA", max(rate.values()))
print_sorted_dict_by_value(rate)
for player in interesting_people:
    print_report(player,report)
print("Введите игрока, на подробный результат которого хотите посмотреть:")
pl = input()
print_report(pl,report)
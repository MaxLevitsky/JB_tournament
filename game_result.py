from game_calculation import calc

print('кол-во игроков:')
n=int(input())
print('кол-во игр:')
k=int(input())
results = []
for i in range(k):
    print(calc(n, i, results))
    results.append([])
    for j in range(n):
        results[i].append(input().split())
    print('Игра обработана')

print(calc(n, k, results))

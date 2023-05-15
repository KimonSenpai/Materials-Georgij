f = open("26_2362.txt")

N, S = map(int, f.readline().split())

items = dict()

for line in f:
    a, b = map(int, line.split())
    if a not in items:
        items[a] = []
    items[a].append(b)
count = 0
cost = 0
for i in items:
    items[i].sort()
    money = S
    for j in items[i]:
        if j <= money:
            money -= j
            count += 1
            cost += j
      

print(count, cost)
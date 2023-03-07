
for file in ("27-A (9).txt", "27-B (9).txt"):
  f = open(file)

  N = int(f.readline())

  res = 0
  mas = [[0]*5 for i in range(2)]

  for line in f:
    val = int(line)

    res += mas[val%2][-val%5]
    mas[val%2][val%5] += 1

  print(res)
'''Найти максимальную сумму пары чисел последовательности,
которая четна и кратна 5'''

for file in ("27-A (9).txt", "27-B (9).txt"):
  f = open(file)

  N = int(f.readline())

  res = 0
  mas = [[0]*5 for i in range(2)]

  for line in f:
    val = int(line)

    res = max(res, val + mas[val%2][-val%5])
    mas[val%2][val%5] = max(mas[val%2][val%5], val)

  print(res)
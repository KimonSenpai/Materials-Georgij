'''
20 10
21 22
'''

for file in ("27-A (10).txt", "27-B (10).txt"):
  f = open(file)

  N = int(f.readline())
  dif = 10000000000000
  s = 0

  for line in f:
    a, b = map(int, line.split())

    s += max(a, b)
    if (a-b) % 3 != 0:
      dif = min(dif, abs(a - b))

  if s % 3 == 0:
    s -= dif
  print(s)
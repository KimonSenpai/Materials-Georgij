
for file in ("27-A_1786.txt", "27-B_1786.txt"):
  f = open(file)
  f.readline()

  sums = [[-1]*10 for _ in range(7)]
  sums[0][0] = 0
  for line in f:
    a, b, c = map(int, line.split())
    new_sums = [[-1]*10 for _ in range(7)]
    for i in range(7):
      for j in range(10):
        if sums[i][j] == -1: continue
        for add in (a + b, a + c, b + c):
          ii = (i + add) % 7
          jj = (j + add) % 10
          new_sums[ii][jj] = max(new_sums[ii][jj], sums[i][j] + add)
    sums = new_sums
  #print([(i,j) for i in range(3) for j in range(3)])
  print(max(sums[i][j] for i in range(7) for j in range(10) if i == 3 and j != 5 or i != 3 and j == 5))
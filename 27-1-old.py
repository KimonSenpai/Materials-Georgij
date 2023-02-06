
f = open("27.txt")

n = int(f.readline())
max_x, max_y = 0, 0
for line in f:
  x, y = map(int, line.split())

  if x == 0:
    max_y = max(max_y, abs(y))
  if y == 0:
    max_x = max(max_x, abs(x))

S = max_x*max_y / 2

if S == 0:
  print("Треугольник не существует")
else:
  print(S)
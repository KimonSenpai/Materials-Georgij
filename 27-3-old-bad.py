k1, k2, k13, k26 = 0, 0, 0, 0

f = open("27.txt")

n = int(f.readline())

for line in f:
  val = int(line)

  if val % 26 == 0:
    k26 += 1
  elif val % 13 == 0:
    k13 += 1
  elif val % 2 == 0:
    k2 += 1
  else:
    k1 += 1

ans = k2*k13 + k26*(k1 + k2 + k13) + k26*(k26-1) // 2
print(ans)
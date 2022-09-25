from math import tan, pi

k = tan(30*pi/180)
cnt = 0

for x in range(1, 11):
  for y in range(11):
    if k*x < y < -k*x + 10:
      cnt += 1

print(cnt)
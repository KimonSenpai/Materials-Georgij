from functools import lru_cache

@lru_cache(None)
def f(a, b):
  if a + b >= 40:
    return -0

  mas = [f(a + 1, b), f(a, b + 1), f(a*2, b), f(a, b*2)]

  if all(v > 0 for v in mas):
    return -max(mas)
  else:
    return -max(v for v in mas if v <= 0) + 1

for s in range(1, 31):
  if f(9, s) == +2:
    print(s)

print()
cnt = 0
for s in range(1, 31):
  if f(9, s) == -2:
    cnt += 1
print(cnt)
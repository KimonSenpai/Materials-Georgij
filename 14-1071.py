
def f(x):
  return 125**200 - 5**x + 74


def count4(val):
  four = 0
  while val > 0:
    if val%5 == 4:
      four += 1
    val //= 5
  
  return four

for x in range(0, 1000):
  if count4(f(x)) == 100:
    print(x)
    exit(0)
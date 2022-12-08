from functools import lru_cache

@lru_cache(False)
def f(n, is_ten):
  if n == 1:
    return int(is_ten)
  if n == 17:
    return 0
  if n == 10:
    is_ten = True
  res = f(n-1, is_ten)

  if n%2 == 0:
    res += f(n//2, is_ten)

  return res

print(f(35, False))
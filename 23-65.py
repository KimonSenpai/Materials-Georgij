from functools import lru_cache

@lru_cache(None)
def dp(s, f):
  if f == s:
    return 1
  if f < s:
    return 0
  
  res = dp(s, f - 1) + dp(s, f - 3)
  if f % 2 == 0:
    res += dp(s, f//2)
  
  return res

print(dp(3, 9)*dp(9, 12)*dp(12, 20))
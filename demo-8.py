
def f(count, prev, is_six = False):
  if count == 0:
    if is_six:
      return 1
    else:
      return 0
  res = 0
  for dig in range(8):
    if count == 5 and dig == 0: continue
    if dig == 6 and is_six: continue
    if prev == 6 and dig % 2 == 1: continue
    if dig == 6 and count != 5 and prev % 2 == 1: continue

    res += f(count - 1, dig, is_six or dig == 6)
  return res

print(f(5, -1))


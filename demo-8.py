

def f(count, last, is_six = False):
  if count == 0:
    return 1
  res = 0
  if last == 6:
    for dig in range(0, 8, 2):
      if dig == 6: continue

      res += f(count - 1, dig, is_six)

    return res
  
  for dig in range(0, 8):
    if count == 5 and dig == 0: continue # костыль
    if dig == 6:
      if last % 2 == 0 and not is_six:
        res += f(count - 1, dig, True)
      else:
        continue
    else:
      res += f(count - 1, dig, is_six)
  return res

print(f(5, -1))


for val in range(210235, 210300 + 1):
  div = 2
  divs = []
  while div*div <= val:
    if val%div == 0:
      divs += [div, val//div]
    div += 1

  divs = list(set(divs))
  divs.sort()
  if len(divs) == 4:
    print(*divs)
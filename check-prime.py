
def check(val):
  div = 2

  while div*div <= val:
    if val % div == 0:
      return False
    div += 1
  
  return True

for i in range(10):
  if check(117 + 4*i):
    print(i)
    break
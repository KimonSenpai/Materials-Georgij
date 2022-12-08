
def gen(length):
  for val in range(10**length):
    if val == 0:
      s = ''
    else:
      s = str(val)
    if len(s) < length:
      s = '0'*(length - len(s)) + s
    
    yield s


for length in range(4):
  for dig in range(10):
    for star in gen(length):
      value = '1' + str(dig) + '2139' + star + '4'
      if int(value)%2023 == 0:
        print(value, int(value) // 2023)
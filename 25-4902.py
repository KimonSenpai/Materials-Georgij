
def construct(ques, star, len_star):
  return (1404 + ques*10)*10**len_star + star

cnt = 0
for len_star in range(3, -1, -1):
  for ques in range(9, -1, -1):
    for star in range(10**len_star - 1, -1, -1):
      val = construct(ques, star, len_star)
      if val % 217 == 0:
        div = 1
        divs = []
        while div*div <= val:
          if val % div == 0:
            divs += [div]
            if div*div != val:
              divs += [val // div]
          div += 1
        divs = [d for d in divs if d % 2 == 1]
        print(val, sum(divs))
        cnt += 1
      if cnt == 7:
        exit(0)
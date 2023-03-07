
mas = [0]*8

f = open("", 'r')

N = int(f.readline())
res = 0
#-5 = p*8 + q, p = -1, q = 3
#val%8 + x = (0 or 8)
#x = ((0 or 8) - val%8)%8 = -val%8
for line in f:
  val = int(line)

  res += mas[-val%8]
  mas[val%8] += 1

print(res)

# val = 59049
# div = 2
# while div*div <= val:
#   d = 0
#   while val % div == 0:
#     d += 1
#     val //= div
#   if d > 0:
#     print(div, d)
#   div += 1
  
# if val > 1:
#   print(val, 1)

# sum:
# a = 4*p_a + q_a, 0 <= q_a < 4, q_a - остаток от деления
# b = 4*p_b + q_b
# (a + b) % 4 == 0 <=> (q_a + q_b) % 4 == 0
f = open("27-B (8).txt")

count_val = [[0]*11 for i in range(4)]
# count_val[i][j] - кол-во чисел с остатком от деления на 4 равным i
# и кратных 3^j

N = f.readline()
pair_count = 0
for line in f:
  val = int(line)
  d = 0
  while val % 3**(d + 1) == 0 and d < 10:
    d += 1
  for j in range(10 - d, 11):
    pair_count += count_val[-val%4][j]
  count_val[val%4][d] += 1
print(pair_count)
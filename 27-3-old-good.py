'''
На вход программы поступает 
последовательность из N целых положительных чисел, 
все числа в последовательности различны. Рассматриваются 
все пары различных элементов последовательности 
(элементы пары не обязаны стоять в последовательности рядом, 
порядок элементов в паре не важен). Необходимо определить 
количество пар, для которых произведение элементов делится 
на 26.
'''


k1, k2, k13, k26 = 0, 0, 0, 0

f = open("27.txt")

n = int(f.readline())
ans = 0
for line in f:
  val = int(line)

  if val % 26 == 0:
    ans += k26 + k13 + k2 + k1
    k26 += 1
  elif val % 13 == 0:
    ans += k2 + k26
    k13 += 1
  elif val % 2 == 0:
    ans += k13 + k26
    k2 += 1
  else:
    ans += k26
    k1 += 1


print(ans)
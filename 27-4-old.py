'''
Последовательность натуральных чисел характеризуется 
числом Y – наибольшим числом, кратным 26 и являющимся 
произведением двух элементов последовательности с различными 
номерами.

Напишите эффективную, в том числе по используемой памяти, 
программу (укажите используемую версию языка программирования, 
например, Borland Pascal 7.0), находящую число Y для 
последовательности натуральных чисел, значение каждого 
элемента которой не превосходит 1000. Программа должна 
напечатать найденное число, если оно существует для заданной 
последовательности, или ноль в противном случае.

Перед текстом программы кратко опишите используемый Вами 
алгоритм решения.

На вход программе в первой строке подаётся количество чисел N. 
В каждой из последующих N строк записано одно натуральное число, 
не превышающее 1000.
'''


k1, k2, k13, k26 = 0, 0, 0, 0

f = open("27.txt")

n = int(f.readline())
ans = 0
for line in f:
  val = int(line)

  if val % 26 == 0:
    ans = max(ans, val*k26, val*k13, val*k2, val*k1)
    k26 = max(k26, val)
  elif val % 13 == 0:
    ans = max(ans, k2*val, k26*val)
    k13 = max(k13, val)
  elif val % 2 == 0:
    ans = max(ans, k13*val, k26*val)
    k2 = max(k2, val)
  else:
    ans = max(ans, k26*val)
    k1 = max(k1, val)


print(ans)
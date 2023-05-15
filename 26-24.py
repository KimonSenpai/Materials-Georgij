f = open('26_24.txt')

s, n = map(int, f.readline().split())

mas = [int(v) for v in f]

mas.sort()

i = 0
while mas[i] <= s:
    s -= mas[i]
    i += 1

print(i)

s += mas[i-1]
print(max(v for v in mas if v <= s))
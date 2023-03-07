f = open("27-7772.txt")

N = int(f.readline())
mas = [0]*8

for i in range(8):
    mas[i] = int(f.readline())

max_elem = 0
max_mul = 0

for i in range(8, N):
    val = int(f.readline())
    max_elem = max(max_elem, mas[i%8])
    max_mul = max(max_mul, val*max_elem)
    mas[i%8] = val

print(max_mul)

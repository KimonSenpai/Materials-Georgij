import random as rd
N = 10**8

f = open('27-7772.txt', 'w')
print(N, file=f)

for i in range(N):
    print(rd.randint(0, 1000), file=f)

f.close()


f = open("27-A_1786.txt")
f.readline()

s = set()
s.add(0)

for line in f:
    a, b, c = map(int, line.split())
    ts = set()
    for val in s:
        ts.add(val + a + b)
        ts.add(val + a + c)
        ts.add(val + c + b)
    s = ts
    if len(s) > 10**7:
        print("RIP")
        exit(0)
res = 0
for val in s:
    if val % 7 == 3 and val % 10 != 5 or \
       val % 7 != 3 and val % 10 == 5:
        res = val

print(res)
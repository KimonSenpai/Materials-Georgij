from functools import lru_cache

def move(n):
    return [f(x) for x in (n + 1, n + 5, 3*n, 6*n)]

@lru_cache(None)
def f(n):
    if n >= 62:
        if n  <= 100:
            return -1
        else:
            return +1
    
    mas = move(n)

    if all (v > 0 for v in mas):
        return -max(mas) - 1
    else:
        return -max(v for v in mas if v < 0) + 1
    
print("Problem 19")
for k in range(1, 62):
    if f(k) in (-2, -3):
        print(k)
        break
    
print("Problem 20")
cnt = 0
for k in range(1, 62):
    if f(k) in (+3, +4):
        cnt += 1
print(cnt)

print("Problem 21")
for k in range(1, 62):
    if f(k) in (-4, -5):
        print(k)

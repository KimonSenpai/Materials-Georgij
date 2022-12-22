def impl(a, b):
  return not a or b

def f(x, A):
  return impl(x%6 == 0, x%10 != 0) or (x + A > 121)


for A in range(1, 200):
  if all(f(x, A) for x in range(1, 200)):
    print(A)
    break
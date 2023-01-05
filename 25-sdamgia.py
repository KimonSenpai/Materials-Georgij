

def is_prime(n):
  div = 2
  while div*div <= n:
    if n % div == 0:
      return False
    div += 1
  return True


# n = sqrt(n)*sqrt(n)
# n = a*b

numb = 1
for val in range(245690, 245756 + 1):
  if is_prime(val):
    print(numb, val)
    numb += 1
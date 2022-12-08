
mas = []
for i in range(1, 6):
  if i % 2 == 0:
    mas += [i**2]

mas = [i**2 for i in range(1, 6) if i % 2 == 0]

print(mas)

print(*(i for i in range(17) if i % 3 == 0))
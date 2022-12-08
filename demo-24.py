
f = open("24.txt", 'r')

s = f.readline() + '$'
f.close()

count = 0
max_count = 0

for c in s:
  if c == 'T':
    count += 1
  else:
    max_count = max(max_count, count)
    count = 0

print(max_count)



f = open("24 (10).txt", 'r')

s = f.readline() + '$'

f.close()

cnt = 0
max_cnt = 0

for c in s:
  if c == '*':
    cnt += 1
  else:
    max_cnt = max(max_cnt, cnt)
    cnt = 0

print(max_cnt)
f = open('26_2362_sorted.txt')
d = f.readline()
s = []
for line in f:
    l = list(map(int,line.split()))
    s.append(l)

fi = open("smth.txt", 'w')
fi.writelines(str(l)+'\n' for l in s)
typeS = 1
count = 34
summ  = 466
for i in range(1,len(s)):
    if s[i][0] == s[i-1][0]:
        if summ - s[i][1] >= 0:
            summ -= s[i][1]
            typeS += 1
            count += s[i][1]
    else:
        summ = 500
        summ -= s[i][1]
        typeS += 1
        count += s[i][1]
print(typeS,count)

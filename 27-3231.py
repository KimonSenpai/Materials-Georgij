

for file in ('27-A_3231.txt', '27-B_3231.txt'):
    f = open(file)
    N = int(f.readline())
    mas = [int(f.readline()) for _ in range(N)]
    def oposit(i):
        global N
        return (i + N//2) % N
    red_sum = 0
    green_sum = 0
    red_cost = 0
    green_cost = 0
    for i in range(1, oposit(0) + 1):
        red_sum += mas[i]
        red_cost += mas[i]*i

    for i in range(0, oposit(0)):
        green_sum += mas[-i]
        green_cost += mas[-i]*i
    index = 1
    min_cost = red_cost + green_cost

    for i in range(1, N):
        green_cost += green_sum - N//2*mas[oposit(i)]
        red_cost += -red_sum + N//2*mas[oposit(i)]

        green_sum += mas[i] - mas[oposit(i)]
        red_sum += -mas[i] + mas[oposit(i)]

        cost = red_cost + green_cost
        if cost < min_cost:
            min_cost = cost
            index = i + 1
    
    print(index)
    
n = int(input())
dp = []
for i in range(n):
    if i == 0:
        dp.append([1])
    elif i == 1:
        dp.append([1, 1])
    else:
        k = [1]
        for j in range(1, i):
            k.append(dp[-1][j - 1] + dp[-1][j])
        k.append(1)
        dp.append(k)
for i in dp:
    print(*i, sep=' ')
    
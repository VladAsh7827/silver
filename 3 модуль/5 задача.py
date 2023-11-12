n, m = map(int, input().split())
dp = []
for i in range(n):
    k = []
    for j in range(m):
        if i == 0 and j == 0:
            k.append(1)
        elif i < 1 or j < 1:
            k.append(0)
        elif (i >= 1 and j >= 2) and (i >= 2 and j >= 1):
            k.append(dp[i - 2][j - 1] + dp[i - 1][j - 2])
        elif i >= 2 and j >= 1:
            k.append(dp[i - 2][j - 1])
        else:
            k.append(dp[i - 1][j - 2])
    dp.append(k)
print(dp[n - 1][m - 1])

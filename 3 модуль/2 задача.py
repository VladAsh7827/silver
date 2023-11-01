n, m = map(int, input().split())
dp = []
for i in range(n):
    a = list(map(int, input().split()))
    dp.append(a)
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] += 0
        elif j - 1 < 0:
            dp[i][j] += dp[i - 1][j]
        elif i == 0:
            dp[i][j] += dp[i][j-1]
        else:
            dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
print(dp[n-1][m-1])
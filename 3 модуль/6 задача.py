n, m = map(int, input().split())
dp = [[0 for j in range(m + 2)] for i in range(n + 2)]
dp[0][0] = 1
for j in range(m):
    i = 0
    a = j
    while i < n and a >= 0:
        dp[i][a] += dp[i - 2][a - 1] + dp[i - 1][a - 2] + dp[i - 2][a + 1] + dp[i + 1][a - 2]
        i += 1
        a -= 1
for i in range(1, n):
    j = m - 1
    a = i
    while a < n and j >= 0:
        dp[a][j] += dp[a - 2][j - 1] + dp[a - 1][j - 2] + dp[a - 2][j + 1] + dp[a + 1][j - 2]
        a += 1
        j -= 1
print(dp[n - 1][m - 1])
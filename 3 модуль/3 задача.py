n, m = map(int, input().split())
a = []
for i in range(n):
    k = list(map(int, input().split()))
    a.append(k)
a[0][0] = (a[0][0], '')
for i in range(n):
    for j in range(m):
        if i < 1 and j < 1:
            pass
        elif i < 1:
            a[i][j] = (a[i][j - 1][0] + a[i][j], a[i][j - 1][1] + 'R')
        elif j < 1:
            a[i][j] = (a[i - 1][j][0] + a[i][j], a[i - 1][j][1] +'D')
        else:
            a[i][j] = max((a[i][j - 1][0] + a[i][j], a[i][j - 1][1] + 'R'), (a[i - 1][j][0] + a[i][j], a[i - 1][j][1] + 'D'))
print(a[n - 1][m - 1][0])
print(*a[n - 1][m - 1][1], sep=' ')

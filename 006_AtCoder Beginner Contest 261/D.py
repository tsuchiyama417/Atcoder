N,M = map(int,input().split())
X = list(map(int,input().split()))
d = {}
for x in range(M):
    c,y = map(int,input().split())
    d[c] = y
dp = [[0 for y in range(N+1)]for x in range(N+1)]
ans = [0 for x in range(N+1)]
dp[0][0] = 0
#x = cointoss number
for x in range(1,N+1):
    dp[x][0] = ans[x-1]
    #y = counta number
    for y in range(1,x+1):
        dp[x][y] = dp[x-1][y-1] + X[x-1]
        if y in d:
            dp[x][y] += d[y]
        ans[x] = max(ans[x],dp[x][y])
#for x in range(N+1):
    #print(*dp[x])
print(max(dp[N]))
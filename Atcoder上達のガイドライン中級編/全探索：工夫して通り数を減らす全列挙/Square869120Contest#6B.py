N = int(input())
A = []
B = []
for i in range(N):
    x, y = (int(x) for x in input().split())
    A.append(x)
    B.append(y)

ans = 1000
sum = 0
for i in range(101):
    for j in range(101):
        for k in range(N):
            sum += (abs(i-A[k]) + abs(B[k]-A[k]) + abs(j - B[k]))
        ans = min(sum, ans)
        sum = 0

print(ans)
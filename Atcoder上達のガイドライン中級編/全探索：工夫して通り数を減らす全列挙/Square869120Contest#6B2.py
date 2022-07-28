import numpy as np

N = int(input())
A = []
B = []
for i in range(N):
    x, y = (int(x) for x in input().split())
    A.append(x)
    B.append(y)

s1 = int(np.median(A))
s2 = int(np.median(B))

ans = 0
for i in range(N):
    ans += abs(s1-A[i]) + abs(B[i]-A[i]) + abs(s2 - B[i])

print(ans)
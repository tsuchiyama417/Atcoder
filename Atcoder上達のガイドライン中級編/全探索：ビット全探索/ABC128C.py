N, M = (int(x) for x in input().split())
d = []
for i in range(M):
    buf = list(map(int,input().split()))
    d.append(buf)
p = list(map(int,input().split()))

c = 0
res = 0
ans = 0
for i in range(2**N):
    L = format(i, 'b').zfill(N)
    
    for j in range(M):
        for k in range(d[j][0]):
            if L[d[j][k+1]-1] == "1":
                c += 1

        if c % 2 == p[j]:
            res += 1
        c = 0

    if res == M:
        ans += 1
    res = 0

print(ans)
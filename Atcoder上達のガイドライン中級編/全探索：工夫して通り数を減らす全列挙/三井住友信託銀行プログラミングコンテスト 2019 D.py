N = int(input())
S = str(input())

ans = 0
S = list(S)
for i in range(1000):
    num = str(i).zfill(3)
    if num[0] in S:
        idx = S.index(num[0])
        S2 = S[(idx+1):]
        if num[1] in S2:
            idx = S2.index(num[1])
            S3 = S2[(idx+1):]
            if num[2] in S3:
                ans += 1

    idx = 0

print(ans)


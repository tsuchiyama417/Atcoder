N, M = (int(x) for x in input().split())

T = []
A = []
for i in range(N):
    var1, var2 = (int(x) for x in input().split())
    T.append(var1)
    A.append(var2)

def sousaand(res,j): 
    ans = format(res & A[j], 'b')
    return int(ans,2)

def sousaor(res,j):
    ans = format(res | A[j], 'b')
    return int(ans,2)

def sousaxor(res,j):
    ans = format(res ^ A[j], 'b')
    return int(ans,2)

res = M
c = 0
for i in range(N):
    if T[i] == 1:
        res = sousaand(res,i)
    if T[i] == 2:
        res = sousaor(res,i)
    if T[i] == 3:
        res = sousaxor(res,i)
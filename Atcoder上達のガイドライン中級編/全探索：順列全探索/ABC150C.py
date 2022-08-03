import itertools

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

L = list(itertools.permutations(range(1, N+1), N))

for i in range(len(L)):
    L[i] = list(L[i])

idxP = L.index(P)
idxQ = L.index(Q)

print(abs(idxP-idxQ))

N = int(input())

A = []
for i in range(N):
    num = int(input())
    x = [int(a) for a in str(num)]
    A.append(x)

print(A)


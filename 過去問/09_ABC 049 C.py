S = str(input())

T = ["dreamer","dream","eraser","erase"]

kiritori = []

for i in range(len(S)-1, -1, -1):
    kiritori.insert(0, S[i])
    res = "".join(kiritori)
    for j in T:
        if res == j:
            S = S[:i]

f = 0
for i in T:
    if i == S:
        f = 1

if f == 1:
    print("YES")
else:
    print("NO")
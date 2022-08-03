import random
L = ["ドド","スコ"]

L2 = []
c = 0
while(1):
    p = random.choice(L)
    L2.append(p)
    print(p, end="")

    if c < 10:
        c += 1
        continue

    if "".join(L2[-12:]) == "ドドスコスコスコドドスコスコスコドドスコスコスコ":
        print("ラブ注入♡")
        exit()

    c += 1


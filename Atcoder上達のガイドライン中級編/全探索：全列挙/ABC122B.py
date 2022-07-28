S = str(input())

c = 0
maxc = 0
for i in S:
    if i == "A" or i =="C" or i =="G" or i =="T":
        c += 1
    else:
        c = 0
    maxc = max(maxc, c) 

print(maxc)
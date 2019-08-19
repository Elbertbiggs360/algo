di = dict()
with open('clown.txt') as hand:
    for lin in hand:
        lin = lin.rstrip()
        wds = lin.split()
        for w in wds:
            di[w] = di.get(w, 0) + 1

sortedList = sorted(di.items(), key=lambda x: x[1], reverse=True)
for val, key in sortedList:
    print(key, val)

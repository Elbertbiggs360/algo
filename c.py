fname = input('File name:')
if len(fname) < 1: fname = 'romeo.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

sortedList = list()
for k, v in di.items():
    reversedItem = (v, k)
    sortedList.append(reversedItem)

sortedList = sorted(sortedList, reverse=True)
for val, key in sortedList[:10]:
    print(key, val)

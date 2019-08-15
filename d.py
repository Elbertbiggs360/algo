fname = input('File name:')
if len(fname) < 1: fname = 'romeo.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

print(sorted([(v,k) for k, v in di.items()], reverse=True)[:10])

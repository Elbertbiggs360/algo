counts = dict()
line = input('Enter a line of text')
words = line.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('List', list(counts))
print('Keys', counts.keys())
print('Items', counts.items())
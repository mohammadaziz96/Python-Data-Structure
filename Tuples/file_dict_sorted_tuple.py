fhand=open("romeo_assignment3.txt")
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word, 0)+1
print(counts)
lst=list()
for key, val in counts.items():
    lst.append((val, key))
lst=sorted(lst, reverse=True)
print(lst)
for val, key in lst[:10]:
    print(key, val)

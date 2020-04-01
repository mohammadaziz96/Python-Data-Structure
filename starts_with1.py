f=open("t.txt", "r")
for i in f:
    i=i.rstrip()
    if not i.startswith("from:"):
        continue
    print(i)

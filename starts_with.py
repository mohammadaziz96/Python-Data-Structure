f=open("t.txt", "r")
for i in f:
    i=i.rstrip()
    if i.startswith("from:"):
        print(i)

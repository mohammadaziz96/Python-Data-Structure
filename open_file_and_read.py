fname=input("Enter your file name: ")
f=open(fname)
count=0
for i in f:
    i=i.rstrip()
    if not i.startswith("because"):
        continue
    print(i)
    count=count+1
print(count)

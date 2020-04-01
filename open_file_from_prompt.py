fname=input("Enter your file name: ")
try:
    f=open(fname)
except:
    print("File can't be opened", fname)
    quit()
count=0
for i in f:
    i=i.rstrip()
    if not i.startswith("because"):
        continue
    print(i)
    count=count+1
print(count)

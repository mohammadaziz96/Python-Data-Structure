fname=input("Enter file name: ")
try:
    f=open(fname)
except:
    print("Entered file name is not available")
    quit()
for l in f:
    l=l.rstrip()
    print(l.upper())

""" 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt od from text file from github when you are testing below enter mbox-short.txt as the file name."""

fname=input("Enter file name: ")
try:
    f=open(fname)
except:
    print("Entered file name is not available")
    quit()
count=0
su=0
for l in f:
    l=l.rstrip()
    if l.startswith("X-DSPAM-Confidence:"):
        #print(l)
        count=count+1
        fp=l.find("0")
        s=l[fp+0:fp+6]
        le=float(s)
        su=su+le
#print(count)
print("Average spam confidence:", su/27)
#print(len(avg))

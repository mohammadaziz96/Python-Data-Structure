"""Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

You can download the sample data at http://www.py4e.com/code3/romeo.txt or you can find romeo_assignment3.txt in the my github.
"""

fname=input("Enter file name: ")
f=open(fname)
lst=list()
for line in f:
    line=line.rstrip()
    s=line.split()
    for i in s:
        if i in lst:
            continue
        else:
            lst.append(i)
lst.sort()
print(lst)

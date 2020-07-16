#An insertion sort is sorting algorithm that sort taking each element comparing with each element untill end of the array.
y=input("How many element you want to sort:")
x=[]
while len(x)<int(y):
    x.append(int(input()))
print("Unsorted Order {}".format(x))
#x=[40,0,12,6,15,51,3,9,21]          #An unordered list
for index in range(1,len(x)): #apply loop over list from index 1 to end
    value=x[index]            #fix a value at 1st index for comparing
    i=index-1                 #0th index for comparing with next value
    while i>=0:               #while loop untill i>=0 
        if value<x[i]:        #if next value is less than previous one
            x[i+1]=x[i]       #swap next value with previous one
            x[i]=value        #swap previous one with fixed value
            i=i-1             # will do for all element in the left
        else:
            break
print("Sorted Order {}".format(x))

# this sorting algorithm is not good because it takes lot time to sort(o(n) time)
# thats why we need to do another algorithm which takes less time

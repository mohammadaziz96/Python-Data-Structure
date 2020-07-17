def sort1(arr):
    while True:
        corrected=False
        for index in range(0, len(arr)-1):
            if arr[index]>arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
                corrected=True
        if not corrected:
            return arr
print(sort1([8,2,0,12,40,3]))

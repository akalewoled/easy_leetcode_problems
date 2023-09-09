arr =[3,4,2,1]
def insertion(arr):
    size = len(arr)
    for i in range (0,size,1):
        low= i
        for j in range(i+1,size,1):
            if (arr[j]< arr[low]):
                low=j
        print (arr)
        temp =arr[i]
        arr[i]=arr[low]
        arr[low]=temp
        
print(insertion(arr))

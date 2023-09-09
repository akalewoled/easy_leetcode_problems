a,b=map(int,input().split())
arr=list(map(int,input().split()))
def kth(arr,k):
    val=arr[k]
    passed=0
    for i in arr:
        if i>=val and i!=0:
            passed+=1 
    return passed
print(kth(arr,b))


# insertion algorithm
print("hello world!")
a = [2,4,6,8,3]

def sort(a):
    c=len(a)
    for i in range(c-1,1,-1):
        
        temp = a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j=j-1
            print("this is the index",i,a)
        a[j+1]=temp
    print(*a)
sort(a)   

def insertsort (a):
    c = len(a)
    for i in range (1,c,1):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp

        print(temp,i,j)
        print(a)

#inverse of insertion sort
def inverseinserionsoert(a):
    c=len(a)
    for i in range(c-2,0,-1):
        temp=a[i]
        j=i+1
        while j<c and a[j]<temp:
            a[j-1]=a[j]
            j=j+1
            print(a)
        a[j-1]= temp
        print(i,j,temp)
    print(a)


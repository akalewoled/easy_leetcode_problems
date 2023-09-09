n,k =map(int,input().split())
a = list(map(int,input().split()))
b=0
for i in range(0,n):
    if a[k-1]==0 and a[i]==a[k-1]:
        b=b+0
    elif a[k-1]<= a[i]:
        b=b+1
    else:
        b=b+0
print(b)
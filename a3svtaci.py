n=int(input())
arr = list(map(int,input().split()))
countof1=0
countof2=0
countof3=0
countof4=0
taxicnt=0
for i in range (0,n):
    if arr[i]==1:
        countof1+=1
    if arr[i]==2:
        countof2+=1
    if arr[i]==3:
        countof3+=1
    if arr[i]==4:
        countof4+=1
taxicnt=countof4
while countof1!=0 and countof3!=0:
    countof3-=1
    countof1-=1
    taxicnt+=1
if countof1==0 and countof3!=0:
    taxicnt+=countof3
taxicnt+=countof2/2
if (countof2%2!=0):
    if countof1<=2:
        taxicnt+=1
        countof1=0
        countof2=0
    else:
        countof1-=2
        countof2=0
        taxicnt+=1
    if countof1!=0:
        taxicnt+=countof1/4
        if countof1%4!=0:
            taxicnt+=1
print(int(taxicnt))







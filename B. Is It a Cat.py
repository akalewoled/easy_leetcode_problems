# first create a funuction to make a stack
def makestack():
    inputword=input()
    arr=[*inputword]
    stack=[]
    yes=True
    for i in arr:
        if i.lower()=='m':
            stack.append(1)
        elif i.lower()=='o':
            stack.append(2)
        elif i.lower()=='e':
            stack.append(3)
        elif i.lower()=='w':
            stack.append(4)
    if stack:
        for k in range(0,len(stack)-1):
            if stack[k]-stack[k-1]>1:
                yes=False
                break
    else:
        yes=False
    return yes

freq=int(input())
res=[]
for i in range(0,freq):
    res.append(makestack())
for i in res:
    print(i)

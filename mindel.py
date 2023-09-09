from collections import *
list=[1,2]

def mode(arr,k):
    res=[]
    count=Counter(arr)
    new_dict=[]
    for key, value in count.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value]=[key]
    keys=new_dict.keys()
    keys1=[]
    keys1+=keys
    keys1.sort()
    for i in range(0,k):
        z=keys1[-1]
        res.append(new_dict[-1])
        keys1.pop()
    print(res)


    return res
print("----strip function ")
a=input("pls enter the stripper function ").strip()
print(a)
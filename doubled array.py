print("welcome")
from collections import *
def cheackchanged(changed):
    counter = Counter(changed)
    res=[]
    for i in counter:
        while(counter[i]>0):
            if i==0:
                if counter[i]%2==0:
                    for j in range(0,counter[i]//2):
                        res.append(i)
                    counter[i]=0
                else:
                    res =[]
                    break
            else:
                if counter[i*2]-counter[i]==0:
                    res.append(i)
                    counter[i]=0
                    counter[i*2]=0
                else:
                    res =[]
                    break
    return res

listes=[0,0,0,0]
print(cheackchanged(listes))
def maxOperations(nums: list[int], k: int) -> int:
    c=Counter(nums)
    output=0
    seen=[]
    for x in c :
        if x not in seen and (k-x) in c:
            output+=min(c[x],c[x-k])
            print(x,seen)
        else:
            output+=min(c[x],c[k-x])
        seen.append(x)
        seen.append(k-x)
    return output
question=[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
print(Counter(question))
k=3
print(maxOperations(question,k))
print("-------------*********************--------------")
# Create a hash map
count=Counter(question)
print(count)
# Get a sorted list of the values in the hash map
sorted_values = sorted(count.values())

rev=dict(reversed(count.items()))

print(sorted_values)
print((rev))

hash_map = {"key1": "value1", "key2": "value2"}

# Reverse the order of the key-value pairs using the OrderedDict class
reversed_hash_map = OrderedDict(reversed(hash_map.items()))

# Check the reversed hash map
print(reversed_hash_map)

# in this task we are given array of intgers we are expected to genrate array of indez of next greter elemnt
def soln(nums):
    print(nums)
    stack=[]
    res=[0]*len(nums)
    i=len(nums)-1
    while i>=0:
        print("for",nums[i])
        if len(stack)==0:
            res[i]==nums[i]
            stack.append(nums[i])
        else:
            leng=0
            while len(stack)>=1 and stack[-1]<=nums[i] :
                print("poped",stack[-1])
                stack.pop()
                leng+=1
                if len(stack)==0:
                    res[i]==nums[i]
                    stack.append(nums[i])
                    break
            res[i]=leng+1
            stack.append(nums[i])
        i-=1
    return res
def clarity(num):
    res=[0]*len(num)
    stack=[]#pair
    print("intial stack",stack)
    for i,t in enumerate(num):
        print("for", t)
        while stack and t >stack[-1][0]:
            stackT, stacki = stack.pop()
            res[stacki]=(i-stacki)
        stack.append([t,i])
        print(stack)
    return res



kk=[73,74,75,71,69,72,76,73]
print(clarity(kk))


print("--------*************---------------")
from collections import OrderedDict
old_dict = {'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23}

# Printing original dictionary
print ("Original dictionary is : ")
print(old_dict)

print()
new_dict = {}
for key, value in old_dict.items():
    if value in new_dict:
        new_dict[value].append(key)
    else:
        new_dict[value]=[key]
print(new_dict)
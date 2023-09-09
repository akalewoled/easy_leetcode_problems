nums=[1,2,3,4]
k=5
i=0
res=0
y=1
while len(nums)>=2 :
    while y<len(nums):
        if nums[0]==nums[y]:
            nums.pop(0)
            nums.pop(y)
            print(nums)
            break
        y+=1

print(res)
for i in range(1,len(nums)):
    if nums[0]==nums[i]:
        nums.pop(0)
        nums.pop(i)
        res+=1
        break
    if i==len(nums):
        nums.pop(0)
        break
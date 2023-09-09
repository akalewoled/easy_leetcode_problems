import collections
a=[2,3,4,5,2,4,5,6,4]
b= collections.Counter(a)
a.sort()

c=[1,2,3,4,5,6,7,8,9]
c.sort()
print(c)
def reverse(list,index):
    for i in range(index // 2):
        list[i], list[index - i - 1] = list[index - i - 1], list[i]
    return list
reverse(c,6)
print(c)
class Solution:
    def reverse(list,index):
        for i in range(index // 2):
            list[i], list[index - i - 1] = list[index - i - 1], list[i]
        return list
        counter=[]

        def pancakeSort(self, arr: List[int]) -> List[int]:
            for i in range (len(arr)-1,0,-1):
                for j in range(i-1,0,-1):
                    if arr[j]>arr[i]:
                        reverse(arr,j)
                        counter.append(j)
                        reverse(arr,i)
                        counter.append(i)
            return counter
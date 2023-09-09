class Solution:
    def kClosest(self, s: List[List[int]], k: int) -> List[List[int]]:
        length=len(s)
        def leng(s):
            x=s[0]
            y=s[1]
            soln=math.sqrt(x*x+y*y)
            return soln
        for i in range (0,len(s)):
            for j in range (i,len(s)):
                if(leng(s[j])<=leng(s[i])):
                    z=s[j]
                    s[j]=s[i]
                    s[i]=z
        a=[[]]
        for m in range(0,k):
            a.append(s[m])
        
        a.pop(0)
        return a
---
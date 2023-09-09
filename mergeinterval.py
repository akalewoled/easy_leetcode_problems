class Solution:
    def sorting(self,a):
        if len(a)<1:
            return a
        else:
            pivot=a.pop()
        small=[]
        large=[]
        for item in a:
            if item[0]>pivot[0]:
                large.append(item)
            else:
                small.append(item)
        return self.sorting(small)+[pivot]+self.sorting(large)
    def merge(self, intervals):
        sorted=self.sorting(intervals)
        result=[]
        for item in sorted:
            if len(result)==0:
                result.append(item)
            else:
                if((item[0]-result[-1][1])<=0):
                    result[-1][1]=item[1]
                else:
                    result.append(item)
        return result
a=[[1,4],[2,3]]
fun=Solution()
k=fun.merge(a)
print(k)

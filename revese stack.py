def reverse(s):
    a=[]
    for i in s:
        if i!=')':
            a.append(i)
        else :
            b=[]
            while a[-1]!='(':
                b.append(a.pop())
            a.pop()
            a=a+b
    return ''.join(map(str, a))
class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[]
        self.size=0
        self.max=k

    def insertFront(self, value: int) -> bool:
        print("inserted",value)

        if self.size < self.max:
            self.deque.insert(0,value)
            return True
        else :
            return False

    def insertLast(self, value: int) -> bool:
        print("inserted",value)
        if self.size < self.max:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.size < self.max:
            self.deque.pop(0)
            self.size-=1
            return True
        else:
            return False


    def deleteLast(self) -> bool:
        if self.size < self.max:
            self.deque.pop()
            return True
        else:
            return False


    def getFront(self) -> int:
        if len(self.deque)>1:
            print(self.deque)
            print("the front",self.deque[1])
            return 0
        else:
            print(self.deque)
            return 0


    def getRear(self) -> int:
        if len(self.deque)>1:
            print("the rear",self.deque[-1])
            return 0
        else:
            print(self.deque)
            return 0


    def isEmpty(self) -> bool:
        return len(self.deque)==0

    def isFull(self) -> bool:
        return self.size==self.max
c=MyCircularDeque(5)
c.insertFront(6)
c.insertFront(6)
c.insertFront(6)
c.insertLast(7)
c.getFront()
kk=[1,2,3]
kk.insert(0,5)
print(len(kk))
def soln(nums):
    stack=[]
    a=len(nums)
    res=[0]*a
    for i in range (len(nums),0,-1):
        if len(stack)==0:
            res[i]==nums[i]
            break
        else:
            len=0
            while stack[-1]<=nums[i]:
                stack.pop()
                len+=1
            if len(stack)==0:
                res[i]==nums[i]
                stack.append(nums[i])
                break
            nums[i]=len+1
            stack.append(nums[i])
    return stack

kk=[2,10,1,2,3,4,5]
print(soln(kk))


""""tokens=["2","1","+","3","*"]
stack=[]
for i  in tokens:
    if  i.isdigit():
        stack.append(i)
    else:
        if len(stack)>=2:
            num1=int(stack.pop())
            num2=int(stack.pop())
            if i=='+':
                res=num1+num2
                stack.append(res)
                print("+   ",stack)
            elif i=='-':
                res=num1-num2
                stack.append(res)
                print("+   ",stack)
            elif i=='*':
                res=num1*num2
                stack.append(res)
                print("+   ",stack)
            elif i=='/':
                if num2==0:
                    raise Exception("divideing to zero err")
                res=num1/num2
                stack.append(res)
                print("+   ",stack)
            else:
                print(num1,num2)
                raise Exception(i, "wrong oprand")
        else:
            print("oprand before operator")
"""
a=["12"]
print(len(a))
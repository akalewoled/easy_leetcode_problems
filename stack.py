
a="[][]{}{[]}"
valid=True
stack1=['a']
for i in a:
    if i=='[':
        stack1.append(i)
    elif i=='{':
        stack1.append(i)
    elif i=='(':
        stack1.append(i)
    elif i==')':
        if stack1[-1]=='(':
            stack1.pop()
        else:
            valid=False
            break
    elif i=='}':
        if stack1[-1]=='{':
            stack1.pop()
        else:
            valid=False
            break
    elif i==']':
        if stack1[-1]=='[':
            stack1.pop()
        else:
            valid=False
if (stack1[-1]!='a'):
    valid=False

print(len(stack1))
print(valid)



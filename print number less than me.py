nums=[4,5,7,4,755,6,4,9]
a = []
for i in nums:
    a.append(len([x for x in nums if x < i]))
    print([x for x in nums if x < i])
print(a)

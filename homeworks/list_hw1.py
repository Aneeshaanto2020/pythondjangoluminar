lst=[2,6,4]
print(lst)
outputlst=[]
for i in lst:
    if i == lst[0]:
        sum1 = lst[1] + lst[2]
        outputlst.append(sum1)
    if i == lst[1]:
        sum2 = lst[0] + lst[2]
        outputlst.append(sum2)
    if i == lst[2]:
        sum3 = lst[0] + lst[1]
        outputlst.append(sum3)
print(outputlst)

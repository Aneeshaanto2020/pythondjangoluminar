num=int(input("enter the number:"))
min=int(input("enter the minimun:"))
max=int(input("enter the maximum:"))
count=0
for i in range(max):
    if i**num in range(min,max+1):
        count += 1
print('Total values found =', count)
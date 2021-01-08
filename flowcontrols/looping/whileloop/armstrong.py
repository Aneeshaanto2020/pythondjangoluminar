num=int(input("enter number:"))
res=0
temp=num
while(temp>0):
    digit=temp%10
    res+=digit**3
    temp//=10
if num==res:
    print("armstrong number...")
else:
    print("not an armstrong number....")

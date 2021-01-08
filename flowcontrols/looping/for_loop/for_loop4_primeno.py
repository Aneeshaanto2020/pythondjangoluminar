num=int(input("enter number:"))
flag=0
if num==1:
    print("not prime number.....")
else:
    for i in range(2,num):
        if(num%i==0):
            flag=flag+1
            break
        else:
            flag=0
    if flag==0:
        print("prime number....")
    else:
        print("not prime number....")

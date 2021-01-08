num=int(input("enter number:"))
lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
for i in range(1,upper):
    res=i**num
    if((lower==res)|(upper==res)):
        print(" ")
    else:
        if(((res>lower)&(res<upper))):
            print(i)
   
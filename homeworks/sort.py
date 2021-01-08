num1=int(input("enter no1"))
num2=int(input("enter no2"))
num3=int(input("enter no3"))
if(num1 < num2):
    if(num1 < num3):
        if(num2 < num3):
            print(num1,",",num1,",",num3)
        else:
            print(num1,",",num3,",",num2)
    else:
        print(num3,",",num1,",",num2)
else:
        if(num2 < num3):
            if(num1 < num3):
                print(num2,",",num1,",",num3)
            else:
                print(num2,",",num3,",",num1)
        else:
            print(num3,",",num2,",",num1)

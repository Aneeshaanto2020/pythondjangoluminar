#without reading numbers
num1=10
num2=20
if(num1>num2):
    print("num1 is largest")
else:
    print("num2 is largest")

#read numbers and print the largest number
num1=int(input("enter no1:"))
num2=int(input("enter no2:"))
if(num1>num2):
    print("num1 is largest")
else:
    print("num2 is largest")

#both numbers are equal
num1=int(input("enter no1:"))
num2=int(input("enter no2:"))
if(num1>num2):
    print("num1 is largest")
elif(num2>num1):
    print("num2 is largest")
elif(num1==num2):
    print("both are equal")

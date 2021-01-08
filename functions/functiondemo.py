# method1
#fn with not return value
def add():
    num1=int(input("enter no1:"))
    num2=int(input("enter no2:"))
    res=num1+num2
    print(res)
add()

print("........................")
# method2
def add(num1,num2): #parameters  => nim1,num2   ,,,,creating fn
    res=num1+num2
    print(res)
add(5,4)  #arguments => 5,4 ,,,,calling fn

print("........................")
#fn with return value

def sub(num1,num2):
    res=num1-num2
    return res
data=sub(100,50)
print(data)

print("........................")

def cube(num):
    return num**3
data=cube(2)
print(data)
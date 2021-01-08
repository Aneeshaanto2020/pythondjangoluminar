num1=int(input("enter no1"))
num2=int(input("enter no2"))
num3=int(input("enter no3"))
if((num1 >= num2) & (num1 >= num3)):
   if(num2 >= num3):
        print("the second largest number",num2)
   else:
        print("the second largest number",num3)
elif((num2 >= num1) & (num2 >= num3)):
  if(num1 >= num3):
         print("the second largest number",num1)
  else:
         print("the second largest number",num3)
elif(num1 >= num2):
     print("the second largest number", num1)
else:
    print("the second largest number",num2)

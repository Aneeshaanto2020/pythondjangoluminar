for row in range(1,5):
    for col in range(1,8):
        if((row==4)|(row+col==5)|(col-row==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()


n=int(input("enter number:"))
for row in range(1,n+1):
    for col in range(1,2*n):
        if((row==n)|(row+col==n+1)|(col-row==n-1)):
            print("*",end="")
        else:
            print(end=" ")
    print()



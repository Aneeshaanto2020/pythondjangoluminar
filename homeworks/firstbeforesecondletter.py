i=occ1=occ2=0
flag = True
#str=int(input("enter the string:"))
#ltr1=int(input("enter the first letter:"))
#ltr2=int(input("enter the second letter:"))
str, ltr1, ltr2 = input('Enter string, first letter and second letter: ').split()
while i<str.count(ltr1):
	if str.find(ltr1,occ1) > str.find(ltr2,occ2):
		flag = False
	occ1,occ2 = str.find(ltr1)+1, str.find(ltr2)+1
	i += 1
if flag:
	print('Check: Success')
else:
	print('Check: Failed')
lst=[1,2,3,4,5]
#      l     u
low=0
upp=len(lst)-1
pair_lst=[]
element=int(input("enter element:")) #4
while(low<upp):#0<3
    tot=lst[low]+lst[upp]
    if(element==tot):
        pair_lst.append((lst[low],lst[upp]))
        upp=upp-1
    elif(element>tot):
        low+=1
    else:
        upp-=1
print(pair_lst)


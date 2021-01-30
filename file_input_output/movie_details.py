f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    number=data[1]
    if(year not in dict):
        dict[year]=number
    else:
        dict[year]=number

for k,v in dict.items():
    print(k,"======>",v)
res=sorted(dict,key=dict.get,reverse=True)
print(res[0],dict.get(res[0]))
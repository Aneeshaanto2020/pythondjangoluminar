expenses={"jan":30000,"feb":25000,"march":25000,"april":22000} #stored as a key value pair format
print(expenses["march"])
#values stored in dict in the form key value pair
#hoe do we fetch value from dictionary
#is to possible to store duplicate ,,,key must be unique
#chk for june20
print("june20" in expenses)


#adding new key value pairs
#june20:25000
expenses["june20"]=25000
print(expenses)

print("march" in expenses)

#update the values
expenses["march"]-=3000
print(expenses["march"])
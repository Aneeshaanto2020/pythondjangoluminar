st1={10,20,30,40}
st2={30,40,50,60,70,80}

#1.Union
#output...10,20.30,40,50,60,70,80
union_set=st1.union(st2)
print(union_set)

#2.Intersection
#output...common elements..i.e .30,40
inter_set=st1.intersection(st2)
print(inter_set)

#3.Difference
#output...st1-st2..i.e...10,20
diff_set=st1.difference(st2)
print(diff_set)
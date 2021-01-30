student={"id":1,"student_name":"aleena","total_mark":30}
if("total_mark" in student):
    print(student["total_mark"])

print(student["student_name"])

if("grade" in student):
    print("exit")
else:
    student["grade"]="A"
print(student)


if(student["total_mark"]>25):
    student["total_mark"]+=5
print(student)
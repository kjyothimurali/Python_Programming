s_no=int(input("enter student number"))
s_name=input("enter student name: ")
summ=0
marks=[]
for i in range(0,3):
    marks.append(int(input("enter marks of subject: ")))
    summ=summ+marks[i]

avg=round(summ/3,2)
print("student no.:",s_no," student name: ",s_name," Marks of 3 subjects: ",marks," total: ",summ," average: ",avg)
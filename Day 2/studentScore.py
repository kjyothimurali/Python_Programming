def result(avg):
    if(avg>=40):
        if(avg<=50):
            return "C"
        elif avg>=51 and avg<=70:
            return "B"
        elif avg>=71 and avg<=80:
            return "A"
        else:
            return "Destension"
    else:
        return "Fail"
    
    
    
s_no=int(input("enter student number"))
s_name=input("enter student name: ")
summ=0
marks=[]
for i in range(0,3):
    marks.append(int(input("enter marks of subject: ")))
    summ=summ+marks[i]

avg=round(summ/3,2)
print("student no.:",s_no," student name: ",s_name," Marks of 3 subjects: ",*marks," total: ",summ," average: ",avg)
print(f"{s_name} got ",result(avg))
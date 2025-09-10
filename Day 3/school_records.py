def add_record(tup):
    
    list_rec.append(tup)

def highest_score():
    h_mark=list_rec[0][2]
    h_name=list_rec[0][1]
    for student in list_rec:
        if student[2]>h_mark:
            h_mark=student[2]
            h_name=student[1]
    print(f"{h_name} got highest marks")


def display_score():
    print("students with marks above 75: ")
    for student in list_rec:
        if (student[2])>75:
            print(f"{student[1]}")

list_rec=[]
print("enter 5 students details")
for i in range(5):
    roll=int(input("roll: "))
    name=input("name: ")
    mark=int(input("marks: "))
    tup=roll,name,mark
    add_record(tup)

highest_score()
display_score()

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll=roll_no
        self.marks=marks
    
    def display(self):
        print("Student Details: ")
        print(f"Name: {self.name}\nroll no: {self.roll}\nmarks: {self.marks}")


student_1=Student("chandra",8,98)
student_1.display()
student_2=Student("jakku",20,89)
student_2.display()

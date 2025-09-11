class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    
    def display(self):
        print("Details...")
        print(f"name: {self._name}\nsalary: {self._salary}")


class Manager(Employee):
    def __init__(self,_name,_salary,department):
        super().__init__(_name,_salary)
        self._department=department

    def display(self):
        super().display()
        print("Department: ",self._department)


emp=Employee("raju",45000)
emp.display()
man=Manager("Ravi",50000,"sales")
man.display()
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def modulus(a,b):
    return a%b

def power(a,b):
    return a**b

x=int(input("enter number x:"))
y=int(input("enter number y:"))
z=add(x,y)
print(f"addition of {x} and {y} is ",z)
z=sub(x,y)
print(f"subtraction of {x} and {y} is ",z)
z=multiply(x,y)
print(f"multiplication of {x} and {y} is ",z)
z=divide(x,y)
print(f"division of {x} and {y} is ",z)
z=modulus(x,y)
print(f"modulus of {x} and {y} is ",z)
z=power(x,y)
print(f"powwer of {x} and {y} is ",z)
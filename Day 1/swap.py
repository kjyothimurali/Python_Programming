#swapping of two numbers
a=int(input("enter for a: "))
b=int(input("enter for b: "))
print("Before swapping: a=",a," b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping: a=",a," b=",b)
#with xor
'''a=a^b
 b=a^b
 a=a^b'''
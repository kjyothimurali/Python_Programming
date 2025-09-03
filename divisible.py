def divisible(n):
    if n%5==0 and n%11==0:
        return True
    else:
        return False
    

num=int(input("enter a number: "))
if(divisible(num)):
    print(f"{num} is divisible by 5 and 11")
else:
    print(f"{num} is not divisible by 5 and 11")
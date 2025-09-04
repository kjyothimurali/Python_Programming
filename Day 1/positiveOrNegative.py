def positiveOrNegative(n):
    return n>0

n=int(input("enter a number"))
if(positiveOrNegative(n)):
    print(f"{n} is positive")
else:
    print(f"{n} is negative")
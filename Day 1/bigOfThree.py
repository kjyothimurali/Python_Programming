def bigOfThree(a,b,c):
    if a>b:
        if a>c:
           return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
a,b,c=map(int,input("enter a,b,c values: ").split())
print(f"biggest of {a},{b},{c} is ",bigOfThree(a,b,c))
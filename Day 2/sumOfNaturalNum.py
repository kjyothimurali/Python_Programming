def sumOfNatural(n):
    i=1
    s=0
    while(i<=n):
        s=s+i
        i=i+1

    return s

n=int(input("enter number"))
print("sum of natural numbers: ",sumOfNatural(n))
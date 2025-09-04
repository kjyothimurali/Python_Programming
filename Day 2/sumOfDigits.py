def sumOfDigits(n):
    res=0
    for i in range(len(str(n))):
        x=n%10
        res=res+x
        n=n//10
    return res


n=int(input("enter a number: "))
print(f"sum of digits in {n} is ",sumOfDigits(n))
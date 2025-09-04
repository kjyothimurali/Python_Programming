def first_last_digit(n):
    
    res=[]
    last=n%10
    while(n>10):
        n=n//10
    res.append(n)
    res.append(last)
    return res


n=int(input("enter a number: "))
arr=first_last_digit(n)
print(f"for number {n} first digit is {arr[0]} and last digit is {arr[len(arr)-1]} ")
s=arr[0]+arr[len(arr)-1]
print(f"sum of first and last digit of {n} is ",s)
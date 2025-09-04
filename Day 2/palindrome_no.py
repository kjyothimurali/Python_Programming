def palindrome(n):
    for i in range(1,n):
        x=i
        z=0
        while(x>0):
            r=x%10
            z=z*10+r
            x=x//10
        if(z==i):
            print(i,end=' ')


n=int(input("enter a number: "))
palindrome(n)
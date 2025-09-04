def strong(n):
    for i in range(1,n):
        x=i
        z=0
        while(x>0):
            r=x%10
            p=1
            while(r>0):
                p=p*r
                r=r-1
            x=x//10
            z=z+p

        if(z==i):
            print(i,end=' ')


n=int(input("enter a number: "))
strong(n)
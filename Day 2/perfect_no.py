def perfect(n):
    for i in range(1,n):
        x=i
        z=0
        for j in range(1,i):
            if i%j==0:
                z=z+j
            
        if(z==i):
            print(i,end=' ')


n=int(input("enter a number: "))
perfect(n)
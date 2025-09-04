def prime(n):
    i=1
    c=0
    count=0
    for i in range(1,n):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c=c+1
        if(c==2):
            print(i,end=' ')
            count=count+1
    
    print("\n",count)
    
n=int(input("enter number : "))
prime(n)
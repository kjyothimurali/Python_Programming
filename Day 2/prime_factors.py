def prime_factors(n):
    for i in range(1,n):
        
        if n%i==0:
            c=0
            for j in range(1,i):
               
                if i%j==0:
                    c=c+1
            if(c==1):
                print(i,end=' ')
            

n=int(input("enter a number: "))
prime_factors(n)
def prime(n):
    i=1
    c=0
    while(i<=n):
        if(n%i==0):
            c=c+1
        i=i+1
        
    if(c==2):
        return "prime"
    else:
        return "not prime"
    
n=int(input("enter number : "))
print(f"{n} is ",prime(n))
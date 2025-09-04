def even_num(n):
    if n%2==0:
        return True
    else:
        return False
    

num=int(input("enter a number"))
if(even_num(num)):
    print("even number")
else:
    print("odd number")
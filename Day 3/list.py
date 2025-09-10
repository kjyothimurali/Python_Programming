def listOp(list_1,n):
    print("enter list elements: ")
    for i in range(n):
        x=input()
        list_1.append(x)

n=int(input("enter size of list: "))
list_1=[]
listOp(list_1,n)
print("list elements are: ",list_1)
    
    
    


def listOp(list_1,n):
    print("enter list elements: ")
    for i in range(n):
        x=int(input())
        list_1.append(x)



def display(list_1):
    print("negative elements: ")
    for i in range(len(list_1)):
        if list_1[i]<0:
            print(list_1[i])


n=int(input("enter size of list: "))
list_1=[]
listOp(list_1,n)
display(list_1)
    
    
    


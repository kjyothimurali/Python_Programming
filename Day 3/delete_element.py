def delete(pos):
    del list_1[pos]


list_1=list(map(int,input("enter list elements: ").split()))
pos=int(input("enter position to delete: "))
delete(pos)
print(list_1)
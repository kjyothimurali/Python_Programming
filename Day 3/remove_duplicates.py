def remove_duplicates(list_1):
    di=[]
    for i in list_1:
        if i not in di:
            di.append(i)
        
    return di
list_1=list(map(int,input().split()))
d=remove_duplicates(list_1)
print(f"list without duplicates :{d}")





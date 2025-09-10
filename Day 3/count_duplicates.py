def count_freq(list_1):
    di={}
    for i in list_1:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    return di
list_1=list(map(int,input().split()))
d=count_freq(list_1)
count=0
for i,j in d.items():
    if j>1:
        count=count+j-1
print(f"total duplicates in list are {count}")

def minimize(string):
    d={}
    for i in range(len(string)):
        if string[i] in d:
            d[string[i]]+=1
        else:
            d[string[i]]=1
    return d
    
string=input("enter a string: ")
s=""
d=minimize(string)
for i,j in d.items():
    s=s+i+str(j)

print(s)
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
max_freq=0

for i,j in d.items():
    if j>max_freq:
        max_freq=j
        s=i

print("highest frequency character is :",s)
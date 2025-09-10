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
min_freq=100000

for i,j in d.items():
    if j<min_freq:
        min_freq=j
        s=i

print("lowest frequency character is :",s)
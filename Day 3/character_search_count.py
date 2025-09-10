def search(string,ch):
    li=[]
    count=0
    for i in range(len(string)) :
        if string[i]==ch:
            count+=1
            li.append(i)
        
    return count,li

s=input("enter a string: ")
ch=input("enter a character to search: ")

res=search(s,ch)
print(f"{ch} occurred {res[0]} times at positions {res[1]}")

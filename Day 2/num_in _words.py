def num_to_words(n):
    res=[]
    if n==0:
        return "zero"
    words={ 1:"one",2:"two",3:"three",4:"four",5:"five",
            6:"six",7:"seven",8:"eight",9:"nine"}
    while(n>0):
        r=n%10
        res.append(words[r])
        n=n//10

    return ' '.join(res[::-1])

n=int(input("ente a number: "))
print(f"{n} in words is ",num_to_words(n))
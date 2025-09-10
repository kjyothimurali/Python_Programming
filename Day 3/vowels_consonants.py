def count_characters(string):
    vow=0
    con=0
   
    li=['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in li:
            vow+=1
        
        else:
            con+=1

    return vow,con


s=input("enter string: ")
t=count_characters(s)
print("vowels:",t[0])
print("consonants:",t[1])

def count_characters(string):
    alpha=0
    digits=0
    special=0
    for i in string:
        if (ord(i)>=65 and ord(i)<=91) or (ord(i)>=97 and ord(i)<=123):
            alpha+=1
        elif ord(i)>=48 and ord(i)<=57:
            digits+=1
        else:
            special+=1

    return alpha,digits,special


s=input("enter string: ")
t=count_characters(s)
print("alphabets:",t[0])
print("digits:",t[1])
print("special chars:",t[2])
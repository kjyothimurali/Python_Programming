def check(ch):
    if(ch>='0' and ch<='9'):
        return "digit"
    elif (ord(ch)>=65 and ord(ch)<=91) or (ord(ch)>=97 and ord(ch)<=122):
        return "alphabet"
    else:
        return "special character"
    

ch=input("enter a character: ")
print(f"{ch} is a ",check(ch))
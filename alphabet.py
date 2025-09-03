def alphabet(ch):
    if (ord(ch)>=65 and ord(ch)<=91) or (ord(ch)>=97 and ord(ch)<=122):
        return True
    else:
        return False
    
ch=input("enter a letter")
if(alphabet(ch)):
    print(f"{ch} is an alphabet")
else:
    print(f"{ch} is not an alphabet")
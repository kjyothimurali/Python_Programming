def length(string):
    count=0
    i=0
    for i in string:
        if i!="\n":
            count+=1
     
   
    return count

def compare(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        return True
    
def concate(s1,s2):
    return s1+s2


s1=input("enter a string 1: ")
s2=input("enter a string 2: ")
print("length of string 1 is ",length(s1))
print(f"{s1} and {s2} are equal: {compare(s1,s2)}")
print(f"concatenation os {s1} and {s2} is {concate(s1,s2)}")
def count_words(string):
    words=string.split(" ")
    count=0
    for i in words:
        count+=1
    
    return count

string=input("enter a string: ")
print("No.of words in string are ",count_words(string))
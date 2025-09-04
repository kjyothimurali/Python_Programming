def count_notes(amt):
   
    count=0
    while(amt>0):
        if(amt>=2000):
            count+=amt//2000
            amt%=2000
        if(amt>=500):
            count+=amt//500
            amt%=500
        if(amt>=200):
            count+=amt//200
            amt%=200
        if(amt>=100):
            count+=amt//100
            amt%100
        if(amt>=50):
            count+=amt//50
            amt%=50
        if(amt>=20):
            count+=amt//20
            amt%=20
        if(amt>=10):
            count+=amt//10
            amt%=10
        if(amt>=5):
            count+=amt//5
            amt%=5
        if(amt>=2):
            count+=amt//2
        else:
            count+=amt//1
            amt%=1
    return count

amt=int(input("enter amount"))
print("total notes: ",count_notes(amt))
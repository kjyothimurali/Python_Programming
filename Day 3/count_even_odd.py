def count_even(li):
    c_even=0
    for i in range(len(li)):
        if li[i]%2==0:
            c_even+=1

    return c_even

def count_odd(li):
    c_odd=0
    for i in range(len(li)):
        if li[i]%2!=0:
            c_odd+=1

    return c_odd



list_1=list(map(int,input("enter list elements: ").split()))
even=count_even(list_1)
odd=count_odd(list_1)
print(f" even numbers are :{even} ant odd numbes are : {odd}")
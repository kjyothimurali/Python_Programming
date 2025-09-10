def second_large(li):
    max_ele=li[0]
    for i in range(1,len(li)):
        if li[i]>max_ele:
            max_ele=li[i]
    sec_lar=li[0]
    for i in range(len(li)):
        if li[i]>sec_lar and li[i]<max_ele:
            sec_lar=li[i]


    return sec_lar


list_1=list(map(int,input("enter elements: ").split()))
x=second_large(list_1)
print(f"second largest element is {x}")
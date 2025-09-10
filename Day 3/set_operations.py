def add_set(ele):
    set1.add(ele)
    



set1=set({})
n=int(input("enter no.of elements:"))
for i in range(n):
    ele=int(input("enter element: "))
    add_set(ele)

print(set1)

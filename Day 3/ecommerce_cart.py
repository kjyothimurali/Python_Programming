def add_product(item):
    cart.append(item)

def remove_product(item):
    cart.remove(item)

def search_product(item):
    if item in cart:
        return True
    else:
        return False
    
def display_cart():
    print(cart)

def count_products():
    count=0
    for item in cart:
        count+=1
    return count

def sort_products():
    print(sorted(cart))

def empty_cart():
    cart.clear()


cart=[]

while True:
    print("cart operations :\n1.add product\n2.remove product\n3.search product\n4.display cart\n5.count products\n6.sort products\n7.clear cart\n8.exit")
    print("enter choice: ")
    ch=int(input())
    if ch==1:
        item=input("enter product to add: ")
        add_product(item)
    elif ch==2:
        item=input("enter product to remove: ")
        remove_product(item)
    elif ch==3:
        item=input("enter product to search: ")
        if search_product(item):
            print(f"product {item} is in the cart.")
        else:
            print(f"product {item} is not in the cart.")
    elif ch==4:
        display_cart()
    elif ch==5:
        print(f"total products : {count_products()}")
    elif ch==6:
        print("sorted order of products : ",sort_products())
    elif ch==7:
        print("cart:",empty_cart())
    elif ch==8:
        print("exiting...")
        break


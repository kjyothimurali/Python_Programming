"""You are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup)."""



def add_book(book_id,title):
    lib[book_id]=title

def remove_book(book_id):
    del lib[book_id]

def search_book(book_id):
    if book_id in lib:
        print("Title of book:",lib[book_id])
    else:
        print("no such book")

def update_title(book_id,new_title):
    lib[book_id]=new_title

def display():
    for i,j in lib.items():
        print(f"{i}---->{j}")
    
def count_books():
    c=0
    for i in lib.keys():
        c+=1
    return c

def check_title(title):
    if title in lib.values():
        return True
    else:
        return False
    

lib={}
while True:
    print("library operations :\n1.add book\n2.remove book\n3.search book\n4.update title\n5.display books\n6.count books\n7.check title\n8.exit")
    print("enter choice: ")
    ch=int(input())
    if ch==1:
        key=input("enter book id : ")
        val=input("enter title")
        add_book(key,val)
    elif ch==2:
        item=input("enter book id to remove: ")
        remove_book(item)
    elif ch==3:
        item=input("enter book id to search: ")
        search_book(item)
    elif ch==4:
        key=input("enter book id : ")
        val=input("enter title")
        update_title(key,val)
    elif ch==5:
        display()
    elif ch==6:
        
        print(f"total books : {count_books()}")
    elif ch==7:
        title=input("enter title to check: ")
        if(check_title(title)):
            print("title is present")
        else:
            print("no title")
  
    elif ch==8:
        print("exiting...")
        break
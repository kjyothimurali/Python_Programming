#converting kilomerters into miles through function
def convert():
    km=int(input("enter no. of kilometers: "))
    miles=round(km*0.621371,2)
    print(km," kilometers in miles are ",miles)

convert()
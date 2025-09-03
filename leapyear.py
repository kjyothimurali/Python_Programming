def leap(year):
    if year%4==0:
        if(year%100==0):
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year=int(input("enter a year"))
if(leap(year)):
    print("leap year")
else:
    print("not leap year")        
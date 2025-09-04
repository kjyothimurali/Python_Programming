#finding week day
def week(day):
    if(day==1):
        return "sunday"
    elif day==2:
        return "monday"
    elif day==3:
        return "tuesday"
    elif day==4:
        return "wednesday"
    elif day==5:
        return "thursday"
    elif day==6:
        return "friday"
    elif day==7:
        return "satureday"
    else:
        return "invalid number"
    
day=int(input("enter week number: "))
weekday=week(day)
print(f"{day} is a ",weekday)

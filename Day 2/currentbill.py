#finding current bill 
def cost(units):
    if(units>=1 and units<=50):
        return (units*3.80)
    elif units>=51 and units<=100:
        return (50*3.80)+((units-50)*4.20)
    elif units>100 and units<=200:
        return (50*3.8)+(50*4.2)+((units-100)*5.10)
    elif units>200 and units<=300:
        return (50*3.8)+(50*4.2)+(100*5.1)+((units-200)*6.30)
    else:
        return (50*3.8)+(50*4.2)+(100*5.1)+(100*6.30)+((units-300)*7.5)
    

cus_no=int(input("enter consumer number: "))
cus_name=input("enter consumer name: ")
pre_reading=int(input("enter present month reading: "))
last_reading=int(input("enter last month reading: "))
tot_units=pre_reading-last_reading
total_cost=cost(tot_units)
print("consumer number: ",cus_no)
print("consumer name: ",cus_name)
print("present month reading : ",pre_reading," units")
print("last month reading: ",last_reading," units")
print("total units consumed: ",pre_reading-last_reading," units")
print("current bill amount: ",total_cost)
print("--------------")
print(f"consumer number is {cus_no} , his name is {cus_name} . His present month reading {pre_reading}, last month reading is {last_reading}. Total units consumed {tot_units} and bill amount is {total_cost}.")
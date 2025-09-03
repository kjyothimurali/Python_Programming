#finding current bill with 3.8 rupees per unit
cus_no=int(input("enter consumer number: "))
cus_name=input("enter consumer name: ")
pre_reading=int(input("enter present month reading: "))
last_reading=int(input("enter last month reading: "))
tot_units=pre_reading-last_reading
total_cost=tot_units*3.80
print("consumer number: ",cus_no)
print("consumer name: ",cus_name)
print("present month reading : ",pre_reading," units")
print("last month reading: ",last_reading," units")
print("total units consumed: ",pre_reading-last_reading," units")
print("current bill amount: ",total_cost," units")
print("--------------")
print(f"consumer number is {cus_no} , his name is {cus_name} . His present month reading {pre_reading}, last month reading is {last_reading}. Total units consumed {tot_units} and bill amount is {total_cost}.")
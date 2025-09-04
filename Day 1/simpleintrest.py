principal_amt=int(input("enter principal amount: "))
rate=int(input("enter rate of intrest per 100: "))
time=int(input("enter time duration in months: "))
si=(principal_amt*time*rate)/100
total=principal_amt+si
print("Simple intrest: ",si," total amount :",total)
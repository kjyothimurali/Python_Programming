"""A 3-day tech workshop collected attendee registrations separately for each day.
 You are given three lists (day1, day2, day3) of email addresses 
 — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
Write a Python program that:
1.Cleans each day's list (normalizes case, removes duplicates).
2.Prints the total number of unique attendees across all days.
3.Prints the list of attendees who attended all three days.
4.Prints the list of attendees who attended exactly one day.
5.Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
6.Produces a final report with counts and sorted lists for each of the above outputs."""


def adding_mails(s,mail):
    s.add(mail.lower())

def total_attendees(s):
    c=0
    for i in s:
        c+=1
    return c

day1=[]
day2=[]
day3=[]
set1=set({})
set2=set({})
set3=set({})
n1=int(input("enter no.of registrations on day1: "))
n2=int(input("enter no.of registrations on day2: "))
n3=int(input("enter no.of registrations on day3: "))

print("enter registered email addresses on day1:")
for i in range(n1):
    mail=input()
    adding_mails(set1,mail)

print("enter registered email addresses on day2:")
for i in range(n2):
    mail=input()
    adding_mails(set2,mail)

print("enter registered email addresses on day3:")
for i in range(n3):
    mail=input()
    adding_mails(set3,mail)

unique_att=(set1|set2)|set3
print(f"Total attendees on 3 days:{total_attendees(unique_att)}")
      
comm_att=(set1&set2)&set3
print(f"attendees on 3 days: {comm_att}")

att=unique_att-(set1&set2)-(set3&set2)-(set1&set3)
print("attendees exactly on one day : ",att)


print("day1 and day2: ",(set1&set2))
print("day2 and day3: ",(set2&set3))
print("day1 and day3: ",(set1&set3))
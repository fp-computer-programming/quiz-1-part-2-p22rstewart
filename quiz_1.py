# Author: Ryan (AMDG) 10/19/21

y = int(input("Enter the year of the date: "))
m = int(input("Enter the month of the date: "))
q = int(input("Enter the day of the date: "))

j = y // 100
k = y % 100

h = (((q + (((26 * (m + 1))) // 10)) + k + (k // 4) + (j // 4) + (5 * j)) % 7)

if m == 3:
    print("March")
elif m == 4:
    print("April")
elif m == 5:
    print("May")
elif m == 6:
    print("June")
elif m == 7:
    print("July")
elif m == 8:
    print("August")
elif m == 9:
    print("September")
elif m == 10:
    print("October")
elif m == 11:
    print("November")
elif m == 12:
    print("December")
elif m == 13:
    print("January")
elif m == 14:
    print("February")

if h == 0:
    print("Saturday")
elif h == 1:
    print("Sunday")
elif h == 2:
    print("Monday")
elif h == 3:
    print("Tuesday")
elif h == 4:
    print("Wenesday")
elif h == 5:
    print("Thursday")
elif h == 6:
    print

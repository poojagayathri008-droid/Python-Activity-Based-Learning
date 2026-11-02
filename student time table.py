a = input("Enter time 1: ")
b = input("Enter time 2: ")

r1 = input("Enter room 1: ")
r2 = input("Enter room 2: ")

if a == b:
    print("Time Conflict")
else:
    print("No Time Conflict")

if r1 == r2:
    print("Room Conflict")
else:
    print("Room Available")

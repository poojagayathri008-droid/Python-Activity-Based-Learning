n = int(input("Enter passengers: "))
total = 0

for i in range(n):
    d = int(input("Enter distance: "))
    age = int(input("Enter age: "))
    c = int(input("Enter class (1 or 2): "))

    fare = d

    if c == 2:
        fare = d * 2
    if age < 12:
        fare = fare / 2

    total = total + fare + 50

print("Total fare:", total)

cancel = input("Cancel ticket? yes/no: ")
if cancel == "yes":
    print("Refund:", total - 100)

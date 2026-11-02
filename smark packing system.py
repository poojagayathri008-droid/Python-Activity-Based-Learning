entry = int(input("Enter entry hour: "))
exit = int(input("Enter exit hour: "))
v = input("Enter vehicle (car/bike): ")

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid time")
else:
    hours = exit - entry

    if hours <= 0:
        hours = hours + 24

    if v == "car":
        fee = hours * 20
    else:
        fee = hours * 10

    if fee > 200:
        fee = 200

    print("Parking fee =", fee)

a = input("Team 1: ")
b = input("Team 2: ")

x = int(input("Team 1 score: "))
y = int(input("Team 2 score: "))

if x > y:
    print(a, "Winner - 3 points")
elif x < y:
    print(b, "Winner - 3 points")
else:
    print("Draw - 1 point each")

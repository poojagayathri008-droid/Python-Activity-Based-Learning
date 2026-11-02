b = 1000
n = int(input("Enter transactions: "))

for i in range(n):
    t = input("D for deposit, W for withdraw: ")
    a = int(input("Enter amount: "))

    if a <= 0:
        print("Invalid amount")
    elif t == "D":
        b = b + a
    elif t == "W" and a <= b and a <= 5000:
        b = b - a
    else:
        print("Transaction rejected")

print("Final balance:", b)

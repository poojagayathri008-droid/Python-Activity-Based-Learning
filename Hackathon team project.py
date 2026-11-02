n = int(input("Enter number of teams: "))
for i in range(n):
    name = input("Team name: ")
    size = int(input("Team size: "))

    if size < 2 or size > 4:
        print("Invalid team size")
        continue

    a = int(input("Round 1 score: "))
    b = int(input("Round 2 score: "))

    total = a + b
    print("Team:", name, "Total:", total)


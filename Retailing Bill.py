a = input("Team 1: ")
b = input("Team 2: ")

x = int(input("Team 1 score: "))
y = int(input("Team 2 score: "))

if x > y:
    p1, p2 = 3, 0
elif x < y:
    p1, p2 = 0, 3
else:
    p1, p2 = 1, 1

print(a, "Points:", p1)
print(b, "Points:", p2)

if p1 > p2:
    print("Winner:", a)
elif p2 > p1:
    print("Winner:", b)
else:
    print("Match Draw")

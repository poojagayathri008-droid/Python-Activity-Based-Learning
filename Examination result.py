a = int(input("Enter marks 1: "))
b = int(input("Enter marks 2: "))
c = int(input("Enter marks 3: "))

if a >= 30 and a < 35:
    a = a + 5
if b >= 30 and b < 35:
    b = b + 5
if c >= 30 and c < 35:
    c = c + 5

print("Total:", a+b+c)

if a >= 35 and b >= 35 and c >= 35:
    print("PASS")
else:
    print("FAIL")

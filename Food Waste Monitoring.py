total = 0
max_waste = 0

for i in range(1, 12):
    prepared = float(input("Food prepared: "))
    served = float(input("Food served: "))

    waste = prepared - served
    percent = (waste / prepared) * 100
    total += percent

    print("Wastage:", waste)
    print("Wastage %:", percent)

    if percent > 10:
        print("HIGH WASTAGE")

    if percent > max_waste:
        max_waste = percent
        max_day = i

print("Average wastage %:", total / 11)
print("Maximum wastage day:", max_day)

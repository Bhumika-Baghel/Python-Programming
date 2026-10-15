a = int(input("Enter base: "))
b = int(input("Enter power: "))

power = 1

for i in range(1, b + 1):
    power = power * a

print(a, "raised to the power", b, "is", power)

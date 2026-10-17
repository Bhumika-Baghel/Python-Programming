print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

ch = int(input("Enter choice: "))
t = float(input("Enter temperature: "))

if ch == 1:
    result = (t * 9 / 5) + 32
    print("Fahrenheit =", result)

elif ch == 2:
    result = (t - 32) * 5 / 9
    print("Celsius =", result)

else:
    print("Invalid choice")

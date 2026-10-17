r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("1. Area")
print("2. Circumference")
print("3. Volume")

choice = int(input("Enter choice: "))

if choice == 1:
    result = 2 * 3.14 * r * (r + h)
    print("Area = {:.2f}".format(result))

elif choice == 2:
    result = 2 * 3.14 * r
    print("Circumference = {:.2f}".format(result))

elif choice == 3:
    result = 3.14 * r * r * h
    print("Volume = {:.2f}".format(result))

else:
    print("Invalid choice")

num = int(input("Enter a number: "))

if num > 0:
    choice = 1
elif num < 0:
    choice = 2
else:
    choice = 3

if choice == 1:
    print("Positive number")
elif choice == 2:
    print("Negative number")
elif choice == 3:
    print("Zero")

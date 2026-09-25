x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if (x == 0 and y == 0):
    print("The point is on origin")
elif (x == 0):
    print("Lies on y-axis")
elif (y == 0):
    print("Lies on x-axis")
else:
    print("The point lies in a quadrant")

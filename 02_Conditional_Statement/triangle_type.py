a = int(input("Enter 1st side of triangle: "))
b = int(input("Enter 2nd side of triangle: "))
c = int(input("Enter 3rd side of triangle: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

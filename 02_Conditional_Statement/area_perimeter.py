l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))

a = l * b
p = 2 * (l + b)

print("Area of rectangle =", a)
print("Perimeter of rectangle =", p)

if (a > p):
    print("Area is greater than perimeter")
else:
    print("Area is not greater than perimeter")

n = int(input("Enter the number: "))
sum = 0
last_digit = 0

while n != 0:
    last_digit = n % 10
    sum = sum + last_digit
    n = n // 10
print("The sum of digit =", sum)

n = int(input("Enter a number: "))

original = n
sum = 0

while (n != 0):
    digit = n % 10
    sum = sum + digit * digit * digit
    n = n // 10

if (sum == original):
    print(original, "is an Armstrong number.")
else:
    print(original, "is not an Armstrong number.")

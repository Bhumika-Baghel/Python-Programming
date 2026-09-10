ch = input("Enter any character: ")

if 'A' <= ch <= 'Z':
    print(f"{ch} is an Uppercase letter.")

elif 'a' <= ch <= 'z':
    print(f"{ch} is a Lowercase letter.")

elif '0' <= ch <= '9':
    print(f"{ch} is a Digit.")

else:
    print(f"{ch} is a Special Character.")

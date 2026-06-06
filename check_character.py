value = input("Enter a value: ")

if value.isalpha():
    print("Alphabet")
elif value.isdigit():
    print("Numeric")
else:
    print("Special Character")
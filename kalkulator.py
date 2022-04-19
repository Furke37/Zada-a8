x = int(input("Enter the value for x: "))

y = int(input("Enter the value for y: "))

operation = input("Choose math operation (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Enter the correct math operation.")
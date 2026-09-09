print("Welcome to Calculator")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose an operation (+ or -): ").strip()

if operation == "+":
    result = add(first_number, second_number)
elif operation == "-":
    result = subtract(first_number, second_number)
else:
    raise ValueError("Operation must be + or -")

print(f"Result: {result}")

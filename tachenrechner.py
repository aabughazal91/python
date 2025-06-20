def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def mod(x, y):
    return x % y

def pow(x, y):
    return x ** y

name = input("Enter your name: ")
print(f"Hello {name.strip().capitalize()}")
print("Welcome to the calculator")

while True:
    try:
        x = float(input("Enter the first number: "))
        operator = input("Select the operator (+, -, *, /, %, **): ")

        if operator not in ["+", "-", "*", "/", "%", "**"]:
            print("Invalid operator. Please select one of the following: + , - , * , / , % , **")
            continue

        y = float(input("Enter the second number: "))

        if operator == "+":
            print(f"{x} + {y} = {add(x, y)}")
        elif operator == "-":
            print(f"{x} - {y} = {sub(x, y)}")
        elif operator == "*":
            print(f"{x} * {y} = {mul(x, y)}")
        elif operator == "/":
            if y == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"{x} / {y} = {div(x, y)}")
        elif operator == "%":
            print(f"{x} % {y} = {mod(x, y)}")
        elif operator == "**":
            print(f"{x} ** {y} = {pow(x, y)}")

        choice = input("Do you want to continue? (yes/no): ").lower().strip()
        if choice != "yes":
            print("Thank you for using the calculator.")
            break

    except ValueError:
        print("Please enter valid numeric inputs.")

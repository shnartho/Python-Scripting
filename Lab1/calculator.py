# Simple Calculator

def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y

print("Welcome to Simple Calculator")
print("1.Plus")
print("2.Minus")
print("3.Multiply")
print("4.Divide")

while True:
    option = input("Enter option(1/2/3/4): ")

    if option in ('1', '2', '3', '4'):
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        if option == '1':
            print(first, "+", second, "=", addition(first, second))

        elif option == '2':
            print(first, "-", second, "=", subtraction(first, second))

        elif option == '3':
            print(first, "*", second, "=", multiplication(first, second))

        elif option == '4':
            print(first, "/", second, "=", division(first, second))

        continue_op = input("Let's do next calculation? (yes/no): ")
        if continue_op == "no":
            break

    else:
        print("Invalid Input")
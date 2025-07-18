def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def main():
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    
    if op == "+":
        print("Result:", add(x, y))
    elif op == "-":
        print("Result:", subtract(x, y))
    elif op == "*":
        print("Result:", multiply(x, y))
    elif op == "/":
        print("Result:", divide(x, y))
    else:
        print("Invalid operation.") 
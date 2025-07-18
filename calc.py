from operations import add, subtract, multiply, divide #This import my functions

def main():
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print ("result = ", add(x, y))
    elif op == '-':
        print(f"result = {subtract(x, y)}")
    elif op == '*':
        print("reult = ", multiply(x, y))
    elif op == '/':
        print(f"result = {divide(x, y)}")
    else:
        print ("Invalid operation")
if __name__ == "__main__":
    main()
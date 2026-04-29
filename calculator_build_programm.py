# calculator build program in python
# their are three basic steps of making calculator in python 
# first step - define a basic function for addition, subtraction, multiplication and division
print("Welcome to the simple calculator program!")
def add(x, y):
    return x + y
def subtract(x, y): 
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y
def average(x, y):
    return (x + y) / 2
# second step - take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Average")  
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# third step - perform the operation based on the user's choice
choice = input("Enter choice(+ ,- ,* ,/ ,avg): ") 
if choice == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '-':
    
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == 'avg':
    print("The average of", num1, "and", num2, "is", average(num1, num2))
else:
    
    print("Invalid input")
    # this is a simple calculator program in python that can perform basic arithmetic operations and also calculate the average of two numbers.   
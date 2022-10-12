from functions import *

#Menu
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")
print("6.Power")
print("7.Square Root")
print("8.Cube Root")
print("9.Factorial")

#Taking input from the user
choice = input("Select your operation (1/2/3/4/5/6/7/8/9): ")

if choice in ('1', '2', '3', '4', '5', '6'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        print(num1, "%", num2, "=", remainder(num1, num2))

    elif choice == '6':
        print(num1, "**", num2, "=", power(num1, num2))
        
elif choice in ('7', '8', '9'):
    num1 = float(input("Enter number: "))

    if choice == '7':
        print("Square root of", num1, "=", square_root(num1))

    elif choice == '8':
        print("Cube root of", num1, "=", cube_root(num1))

    elif choice == '9':
        print("Factorial of", num1, "=", factorial(num1))
        
else:
    print("Invalid Input, please try again")
    
    

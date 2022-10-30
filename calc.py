# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
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
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
Run Code
Output

Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice(1/2/3/4): 3
Enter first number: 15
Enter second number: 14
15.0 * 14.0 = 210.0
Let's do next calculation? (yes/no): no
In this program, we ask the user to choose an operation. Options 1, 2, 3, and 4 are valid. If any other input is given, Invalid Input is displayed and the loop continues until a valid option is selected.

Two numbers are taken and an if...elif...else branching is used to execute a particular section. User-defined functions add(), subtract(), multiply() and divide() evaluate respective operations and display the output.

Share on:
Did you find this article helpful?
Related Examples
Python Example

Find the Largest Among Three Numbers

Python Example

Add Two Numbers

Python Tutorial

Python User-defined Functions

Python Example

Find LCM


Join our newsletter for the latest updates.
Enter Email Address*
Join


Tutorials
Python 3 Tutorial
JavaScript Tutorial
SQL Tutorial
C Tutorial
Java Tutorial
Kotlin Tutorial
C++ Tutorial
Swift Tutorial
C# Tutorial
Go Tutorial
DSA Tutorial
Examples
Python Examples
JavaScript Examples
C Examples
Java Examples
Kotlin Examples
C++ Examples
Company
About
Advertising
Privacy Policy
Terms & Conditions
Contact
Blog
Youtube
Apps
Learn Python
Learn C Programming
Learn Java
© Parewa Labs Pvt. Ltd. All rights reserved.

   

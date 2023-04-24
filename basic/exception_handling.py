"""_exception_
In Python, an exception is an error that occurs during the execution of a program. 
When an error occurs, Python raises an exception, which can be caught and handled by the program.
"""

"""_try, except_
When an exception is raised in Python, the program will stop executing 
unless the exception is caught and handled by the program. 
This can be done using a 'try' block and an accompanying 'except' block. 
The try block is used to enclose the code that may raise an exception, 
while the except block is used to catch and handle the exception if it occurs.
"""

### 1. Handling a specific exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print('Cannot devide by zero')
    
### 2. Handling multiple exceptions
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
### 3. Handling any exception with a generic block
try:
    x = 10 / 0
except Exception as e:
    print("An error occurred:", e)

"""_finally_ 
(Optional) The keyword 'finally' is always executed after try and except blocks.
In the below example, you can use a 'finally' block to ensure that the file is closed 
regardless of whether an exception was caught or not.
"""

### 4. Using the finally block
try:
    file = open("./myfile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

"""_raise_
This 'raise' keyword allows us to create our own custom exceptions for situations 
that are not covered by the built-in Python exceptions.
"""

### 5. Raising an exception
x = -1
if x < 0:
    raise ValueError("Number must be positive")

"""_else_
(Optional) If no exception is raised in the try block, 
the code in the else block will execute, 
in the below example, printing the result of the division.
"""

### 6. Using the else block
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("The result is:", y)
finally:
    print("This code always executes")
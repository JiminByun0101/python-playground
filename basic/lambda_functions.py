# Normal def defined function
def add(a, b):
    return a + b
result = add(1,2)
print(result)   # Output: 3

# Lambda
add = lambda a, b: a + b
result = add(1,3)
print(result)  # Output: 4

result = (lambda a, b: a + b)(1,4)
print(result)  # Output: 5

result = (lambda a, b: a + b)(a=1,b=4)
print(result)  # Output: 5

result = (lambda a, b=4: a + b)(1)
print(result)  # Output: 5

# Using if-else in lambda function
print((lambda a, b: a if a%2 == 0 else b)(1,3))   # Output: 3

# Using String format() in lambda function
print((lambda a, b: '{} + {} = {}'.format(a,b,a+b)) (1,5))  # Output: "1 + 5 = 6"

# Sorting a list using lambda
data = ['Python Lambda', 'Python', 'Hello World' ]
data.sort(key=lambda x: len(x))
print(data)  # Output: ['Python', 'Hello World', 'Python Lambda']

# Creating a new list using lambda
data = list(map(lambda x: x*2, range(10)))
print(data)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Filtering using lambda
data = list(filter(lambda x: x % 2 == 0, range(10)))
print(data)  # Output: [0, 2, 4, 6, 8]

# Returning lambda
def calc(op):
    if op == '+':
        return lambda a, b: a + b
    elif op == '-':
        return lambda a, b: a - b
    elif op == '*':
        return lambda a, b: a * b
    elif op == '/':
        return lambda a, b: a / b
    else:
        return lambda a, b: a % b
myCalc = calc('+')
print(myCalc(1,6))  # Output: 7

# Recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # Output: 120

fact = lambda n : 1 if n == 1 else n * fact(n-1) 
print(fact(5))  # Output: 120
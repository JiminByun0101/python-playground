### Creating a list
# create an empty list
my_list = []
print(my_list)  # []

# create a list with some initial values
my_list = [1, 2, 3, 4, 5]
print(my_list)  # [1, 2, 3, 4, 5]

# create a list with mixed data types
my_list = [1, "hello", True, 3.14]
print(my_list)  # [1, "hello", True, 3.14]

### Accessing list elements
# access the first element of the list (at index 0)
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # 1

# access the last element of the list (at index -1)
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])  # 5

# access a slice of the list (from index 1 to 3)
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # [2, 3, 4]

### Modifying list elements
# update the value of an element at a specific index
my_list = [1, 2, 3, 4, 5]
my_list[2] = "hello"
print(my_list)  # [1, 2, "hello", 4, 5]

# append an element to the end of the list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  # [1, 2, 3, 4, 5, 6]

# remove an element from the list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # [1, 2, 4, 5]

# extend a list by adding multiple elements at the end using extend() method
var = [1, 2, 3, 4]
var.extend([10, 11, 12])
print(var) # [1, 2, 3, 4, 10, 11, 12]

# insert an element at a specific index using insert() method
var.insert(0, 0)
print(var) # [0, 1, 2, 3, 4, 10, 11, 12]

# remove and return the last element of the list using pop() method
var.pop()
print(var) # [0, 1, 2, 3, 4, 10, 11]
var.pop(0)
print(var) # [1, 2, 3, 4, 10, 11]

# count the occurrences of an element in the list using count() method
var = var * 2
print(var.count(2)) # 2

# find the index of an element in the list using index() method
print(var.index(10)) # 4
try:
    print(var.index(6))  # Output: Raises a ValueError since 6 is not in the list
except ValueError:
    print('ValueError')

### List operations
# concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5, 6]

# find the length of a list
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # 5

# check if an element is in the list
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True

# repeat a list a certain number of times
my_list = [1, 2, 3]
result = my_list * 3
print(result)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

### A list can contain any Python type
# create a list with different types of data
var = [1, 'chris', ['tommy', 'harry'], ('hans', 2)]

# print the entire list
print(var) # [1, 'chris', ['tommy', 'harry'], ('hans', 2)]

# access the last element of the list
print(var[3]) # ('hans', 2)

# access the first element of the nested list inside the main list
print(var[2][0]) # 'tommy'

# access the last element of the list using negative indexing
print(var[-1]) # ('hans', 2)

# modify the first element of the list
var[0] = 7
print(var[:2]) # [7, 'chris']

# delete elements from the list
del var[2:]
print(var) # [7, 'chris']

### List Methods
# sort() method sorts the elements of a list in ascending order. It modifies the original list.
import random
var = list()
for i in range(10):
    var.append(random.randint(1, 100))  # Generating random numbers between 1 and 100
print(var)  # Output: [18, 76, 29, 69, 11, 94, 41, 80, 22, 85]

# var.sort()
print(var)  # Output: [11, 18, 22, 29, 41, 69, 76, 80, 85, 94]

# reverse() method reverses the order of elements in the list. It modifies the original list.
var.reverse()
print(var)  # Output: [94, 85, 80, 76, 69, 41, 29, 22, 18, 11]

# clear() method removes all the elements from the list. It modifies the original list.
var.clear()
print(var)  # Output: []

# List Comprehension is a concise way of creating a list.
# Here, we create a list of even numbers between 1 and 10.
var = []
# var = list()
for data in range(1, 11):
    if data % 2 == 0:
        var.append(data)
print(var)  # Output: [2, 4, 6, 8, 10]

# We can achieve the same result as above using filter() and lambda functions.
var = list(filter(lambda x: x % 2 == 0, range(11)))
print(var)  # Output: [0, 2, 4, 6, 8, 10]

# We can also achieve the same result as above using list comprehension.
var = [data for data in range(1, 11) if data % 2 == 0]
print(var)  # Output: [2, 4, 6, 8, 10]

# List Comprehension can be used to create lists of tuples as well.
# Here, we create a list of all possible combinations of (x, y) where x and y are between 1 and 10,
# and their sum is equal to 10.
var = [(x, y) for x in range(1, 11) for y in range(1, 11) if x + y == 10]
print(var)  # Output: [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]

# List Comprehension can have multiple conditions.
# Here, we create a list of even numbers between 1 and 10, which are greater than 5.
var = [x for x in range(1, 11) if x % 2 == 0 if 5 < x]
print(var)  # Output: [6, 8, 10]

"""_generator_
is a type of iterable, like a list or a tuple. 
It allows you to iterate over a sequence of values 
without actually creating the entire sequence in memory at once. Instead, 
it generates each value on-the-fly as you request it.
"""
# Define a generator expression that adds 10 to each even number from 1 to 10
var = (data + 10 for data in range(1,11) if data % 2 == 0)

# Print the generator object
print(var)  # Output: <generator object <genexpr> at 0x7f98a2c8da50>

# Use the next() function to print the first five values generated by the generator
try:
    print(next(var))  # Output: 12
    print(next(var))  # Output: 14
    print(next(var))  # Output: 16
    print(next(var))  # Output: 18
    print(next(var))  # Output: 20
    
    # This next() call will raise a StopIteration exception because there are no more values to generate
    print(next(var))
except StopIteration:
    print('StopIteration')  # Output: StopIteration

"""_Stack_
A stack is a collection of elements that supports two basic operations: 
push, which adds an element to the top of the stack, 
and pop, which removes the top element from the stack.
"""
# Create a list representing a stack with three elements
stack = [1, 2, 3]

# Push two more elements onto the stack
stack.append(4)
stack.append(5)

# Print the current contents of the stack
print(stack)  # Output: [1, 2, 3, 4, 5]

# Pop one element from the stack and print it
var = stack.pop()
print(var)  # Output: 5

# Print the updated contents of the stack
print(stack)  # Output: [1, 2, 3, 4]

# Pop another element from the stack and print it
var = stack.pop()
print(var)  # Output: 4

# Print the final contents of the stack
print(stack)  # Output: [1, 2, 3]

"""_Queue_
A queue is a collection of elements that supports two basic operations: 
enqueue, which adds an element to the back of the queue, 
and dequeue, which removes an element from the front of the queue.
"""
# Import the deque class from the collections module
from collections import deque

# Create a deque representing a queue with three elements
queue = deque(["chris", "tommy", "harry"])

# Enqueue one more element onto the back of the queue
queue.append("hans")

# Print the current contents of the queue
print(queue)  # Output: deque(['chris', 'tommy', 'harry', 'hans'])

# Dequeue one element from the front of the queue and print it
var = queue.popleft()
print(var)  # Output: chris

# Print the updated contents of the queue
print(queue)  # Output: deque(['tommy', 'harry', 'hans'])

# Dequeue another element from the front of the queue and print it
var = queue.popleft()
print(var)  # Output: tommy

# Print the final contents of the queue
print(queue)  # Output: deque(['harry', 'hans'])

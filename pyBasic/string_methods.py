# type()
str = 'Hello World'
print(type(str))  # Output: <class 'str'>

# len()
str = 'Hello World'
print(len(str))  # Output: 11

# count()
str = 'Hello World'
print(str.count('l'))  # Output: 3

"""_find()_
This method returns the 'index' of the first occurrence 
of a specified substring in a string, 
or -1 if the substring is not found.
"""
str = 'Hello My World'
print(str.find('My'))  # Output: 6
print(str.find('Your'))  # Output: -1

"""_rfind()_
This method returns the index of the last occurrence 
of a specified substring in a string. 
If the substring is not found, it returns -1. 
The r in rfind stands for "right", 
indicating that the search starts from the right side of the string.
"""
str = 'Hello My World'
print(str.rfind('o'))  # Output: 10

"""_index()_
This method returns the index of the first occurrence 
of a specified substring in a string. 
If the substring is not found, it raises a 'ValueError' exception.
"""
str = 'Hello My World'
try:
    print(str.index('Your'))
except ValueError as e:
    print(e)  # Output: "substring not found"
    
"""_join()_
This method joins a list of substrings 
with a specified delimiter to form a new string.
"""
str = '-'.join('Hello')
print(str)  # Output: "H-e-l-l-o"

strings = ["hello", "world"]
joined_string = " ".join(strings)
print(joined_string)  # Output: "hello world"

# upper()
str = 'Hello World'
print(str.upper())  # Output: "HELLO WORLD"

# lower(0)
str = 'Hello World'
print(str.lower())  # Output: "hello world"

"""_strip()_
This method returns a new string 
with any leading or trailing whitespace removed.
"""
str = '    Hello World   '
print(str.strip())

# lstrip()
str = '    Hello World   '
print(str.lstrip())

# rstrip()
str = '    Hello World   '
print(str.rstrip())

# replace()
str = 'Hello My World'
print(str.replace('My', 'Your'))  # Output: "Hello Your World"

"""_split()_
his method returns a list of substrings 
separated by a specified delimiter.
"""
str = 'Hello My World'
print(str.split(' '))  # Output: ['Hello', 'My', 'World']

str = 'Hello-Your-World'
print(str.split('-', 1))  # Output: ['Hello', 'Your-World']

# zfill()
str = 'Start'
print(str.zfill(10))  # Output: "00000Start"

# rjust()
str = 'Start'
print(str.rjust(10, '1'))  # Output: "11111Start"

# ljust()
str = 'Start'
print(str.ljust(10, '1'))  # Output: "Start11111"

# center()
str = 'Start'
print(str.center(10, '-'))  # Output: "--Start---"

# How to reverse a String in Python (1)
str = 'Hello World'
reversed_str = ''
for c in str:
    reversed_str = c + reversed_str
print(reversed_str)

# How to reverse a String in Python (2)
str = 'Hello World'
str_list = list(str)
str_list.reverse()
reversed_str = ''.join(str_list)
print(reversed_str)

# How to reverse a String in Python (3)
str = 'Hello World'
reversed_str = str[::-1]
print(reversed_str)
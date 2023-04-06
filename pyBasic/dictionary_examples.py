# Dictionary
var = {'name' : 'chris', 'age' : 23, 1 : ['a' , 'b', 'c']}  # create a dictionary with string, integer, and list values
print(var)  # {'name': 'chris', 'age': 23, 1: ['a', 'b', 'c']}
print(var['name'])  # chris

var['age'] = 33  # modify the value of a key
print(var)  # {'name': 'chris', 'age': 33, 1: ['a', 'b', 'c']}

del var[1]  # remove a key-value pair
print(var)  # {'name': 'chris', 'age': 33}

var[1] = 'Hi'  # add a new key-value pair
print(var)  # {'name': 'chris', 'age': 33, 1: 'Hi'}

var.update({'name' : 'hans', 'age' : 30})  # update multiple keys' values at once
print(var)  # {'name': 'hans', 'age': 30, 1: 'Hi'}

data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = {'3rd' : 'hans', '4th' : 'james', '5th' : 'jenny'}
var = {**data_1, **data_2}  # merge two dictionaries using the ** operator
print(var)  # {'1st': 'chris', '2nd': 'tommy', '3rd': 'hans', '4th': 'james', '5th': 'jenny'}

# var = data_1 | data_2  # equivalent to merging dictionaries using the | operator (Python 3.9+)
# print(var)  # {'1st': 'chris', '2nd': 'tommy', '3rd': 'hans', '4th': 'james', '5th': 'jenny'}


### Shallow and Deep Copy
# Creating a dictionary and assigning it to two different variables
data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1

# Printing both dictionaries, they should be identical
print(data_1)  # Output: {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}
print(data_2)  # Output: {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}

# Modifying one of the dictionaries
data_1['1st'] = 'hans'

# Printing both dictionaries again, data_1 has changed, but data_2 is still the same
print(data_1)  # Output: {'1st': 'hans', '2nd': 'tommy', '3rd': 'harry'}
print(data_2)  # Output: {'1st': 'hans', '2nd': 'tommy', '3rd': 'harry'}

# Creating a new dictionary that is a copy of the original dictionary
data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1.copy()

# Printing both dictionaries, they should be identical
print(data_1)  # Output: {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}
print(data_2)  # Output: {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}

# Modifying one of the dictionaries
data_1['1st'] = 'hans'

# Printing both dictionaries again, data_1 has changed, but data_2 is still the same
print(data_1)  # Output: {'1st': 'hans', '2nd': 'tommy', '3rd': 'harry'}
print(data_2)  # Output: {'1st': 'chris', '2nd': 'tommy', '3rd': 'harry'}

# Creating a dictionary
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print(var)  # Output: {'chris': 10, 'tommy': 30, 'harry': 20}

### Dictionary Comprehesion
# Using dictionary comprehension to create a new dictionary with only values less than 20
var = { name : age for name, age in var.items() if age < 20}
print(var)  # Output: {'chris': 10}

### Using dictionary methods
# The keys() method returns a view object that contains the keys of the dictionary
var = {'chris': 10, 'tommy': 30, 'harry': 20}
print(var.keys()) # dict_keys(['chris', 'tommy', 'harry'])

# The values() method returns a view object that contains the values of the dictionary
print(var.values()) # dict_values([10, 30, 20])

# The items() method returns a view object that contains the (key, value) pairs of the dictionary
print(var.items()) # dict_items([('chris', 10), ('tommy', 30), ('harry', 20)])

# The clear() method removes all items from the dictionary
var.clear()
print(var) # {}

# The get() method returns the value of the specified key in the dictionary
# If the key does not exist, it returns None by default
var = {'chris': 10, 'tommy': 30, 'harry': 20}
print('chris' in var) # True
print(var.get('chris')) # 10
print('hans' in var) # False
print(var.get('hans')) # None
print(var.get('hans', 'hans is not in var')) # 'hans is not in var'

### Iterable methods

# The items() method can also be used to iterate over the (key, value) pairs of the dictionary
var = {'chris': 10, 'tommy': 30, 'harry': 20}
for k, v in var.items():
    print(k, v) # chris 10, tommy 30, harry 20

# The enumerate() function can be used to iterate over a sequence with an index
for i, v in enumerate(['chris', 'tommy', 'harry']):
    print(i, v) # 0 chris, 1 tommy, 2 harry

# The zip() function can be used to iterate over multiple sequences in parallel
name = ['chris', 'tommy', 'harry']
age = [10, 30, 20]
for k, v in zip(name, age):
    print(k, v) # chris 10, tommy 30, harry 20

### JSON methods

# The json module provides methods for encoding and decoding JSON data

# The json.loads() method decodes a JSON string into a Python object
import json
var = '{"chris": 10, "tommy": 30, "harry": 20}'
print(var) # {"chris": 10, "tommy": 30, "harry": 20}
print(type(var)) # <class 'str'>
var = json.loads(var)
print(var) # {'chris': 10, 'tommy': 30, 'harry': 20}
print(type(var)) # <class 'dict'>

# The json.dumps() method encodes a Python object into a JSON string
var = json.dumps(var)
print(var) # {"chris": 10, "tommy": 30, "harry": 20}
print(type(var)) # <class 'str'>

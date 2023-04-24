"""_Faker_
is a Python library that allows you to generate fake data in a variety of formats, such as names, addresses, phone numbers, and more. 
This can be useful for a variety of applications, such as testing, prototyping, or generating sample data.
"""

from faker import Faker

# Create an instance of the Faker class
fake = Faker()

### 1. Generating Fake Names
# Generate a randon name
name = fake.name()
print(name)

# Generate a random first name
first_name = fake.first_name()
print(first_name)

# Generate a random last name
last_name = fake.last_name()
print(last_name)

"""_result_
Kelly Farrell
Deborah
Jones
"""

### 2. Generating Fake Addresses
# Generate a random street address
address = fake.street_address()
print(address)

# Generate a random city
city = fake.city()
print(city)

# Generate a random state
state = fake.state()
print(state)

# Generate a random zip code
zip_code = fake.zipcode()
print(zip_code)

"""_result_
3558 Cobb Valley Suite 311
Kennethview
Nebraska
87785
"""

### 3. Generating Fake Text
# Generate a random sentence
sentence = fake.sentence()
print(sentence)

# Generate a random paragraph
paragraph = fake.paragraph()
print(paragraph)

# Generate a random text
text = fake.text()
print(text)

"""_result_
Leave behavior life back begin.
Better age out cover structure. Keep report condition. Majority though only skin three.
Upon house close learn land. Any conference decide small boy century lawyer. Be carry citizen stock expect south plan.
"""
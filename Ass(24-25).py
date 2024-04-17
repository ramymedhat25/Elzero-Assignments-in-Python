# Task 1
# Needed Output
# "Osama"
# <class 'tuple'>

tuple1=("Osama")
print(tuple1)
print(type((tuple1,)))

# Task 2
friends = ("Osama", "Ahmed", "Sayed")

# Needed Output
# ("Elzero", "Ahmed", "Sayed")
friends = ("Elzero",) + friends[1:]
print(friends)
# <class 'tuple'>
print(type(friends))
# 3 Elements
print(len(friends), "Elements")


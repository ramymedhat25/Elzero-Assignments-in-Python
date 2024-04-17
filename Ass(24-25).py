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


# Task 3
nums = (1, 2, 3)
letters = ("A", "B", "C")
# Needed Output
# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
new = nums + letters 
print(new)
# 6 Elements
print(len(new), "Elements")
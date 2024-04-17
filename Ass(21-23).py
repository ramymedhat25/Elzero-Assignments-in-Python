# Task 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print (friends[0])
print(friends[friends.index('Osama')])
print(friends.pop(0))


print(friends[-1])
print(friends[friends.index('Mahmoud')])
print(friends.pop(-1))

# Task 2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"

print (friends[::2])
print (friends[1::2])

# Task 3
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"

print (friends[1:4:1])
print (friends[3::1])


# Task 4
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]

friends[-2:] = ["Elzero", "Elzero"]

print(friends)

# task 5
friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.append("Salem")
print(friends)

# task 6 
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
print(friends[2:])
# ["Ahmed", "Sayed"]
print(friends[2:4])

# task 7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)


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

# 
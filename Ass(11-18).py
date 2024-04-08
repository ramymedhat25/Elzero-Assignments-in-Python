# Task 1
Name = "Ramy"
Age = "25"
Country = "Egypt"

print("Hello '", Name, "', How You Doing \\\"\" Your Age Is \"", Age, "\" + And Your Country Is:", Country)


# Task 2
print("Hello '", Name, "', How You Doing \\\"\"  \nYour Age Is \"", Age, "\" + \nAnd Your Country Is:", Country)

# Task 3

name = 'Elzero'
# Needed Output
# Second Letter Is "l"
print(name[1])
# Third Letter Is "z"
print(name[2])
# Last Letter Is "o"
print(name[-1])

# Task 4
name = 'Elzero'
# Needed Output
# "lze"
print(name[1:4])
# "Ezr"
print(name[::2])
# "rzE"
print(name[-2::-2])

# Task 5

name = "#@#@Elzero#@#@"

print(name.strip("@#"))

# Task 6

num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

# Task 7
name_one = "Osama"
print(name_one.rjust(20,"@"))

name_two = "Osama_Elzero"
print(name_two.rjust(20,"@"))
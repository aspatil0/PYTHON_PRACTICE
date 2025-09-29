# Python List Example

# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Printing the list
print("Original List:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Inserting element at a position
fruits.insert(2, "grapes")
print("After insert:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Popping last element
last = fruits.pop()
print("Popped:", last)
print("After pop:", fruits)

# Slicing
print("First two fruits:", fruits[:2])

# Iterating through list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# List comprehension (make all fruits uppercase)
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)

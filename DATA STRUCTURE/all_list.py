
fruits = ["apple", "banana", "cherry", "mango"]

print("Original List:", fruits)

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

print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# List comprehension (make all fruits uppercase)
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)

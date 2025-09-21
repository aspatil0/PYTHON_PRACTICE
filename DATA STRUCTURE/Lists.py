# A list in Python is a built-in data type used to store an ordered collection of items
#Lists are ordered
#Lists are mutable
#Lists allow duplicate values

#Lists can hold different data types in a single list (e.g., integers, strings, floats, etc)
#Lists are defined using square brackets []

#Creating a list
my_list = [1, 2, 3, "hello", 4.5, True]
print(my_list)

#Accessing elements in a list
print(my_list[0]) 




#adding elements to a list
my_list.append(6)  #last
print(my_list)

my_list.insert(0, "world")  #index
print(my_list)

my_list.extend([7, 8, 9])  #multiple elements
print(my_list)

new_list = [10, 11]
my_list = my_list + new_list  #concatenation
print(my_list)


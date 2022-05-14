# returns the length of a list
my_collection = [1, 1, 12, False, "Hi"]
print(len(my_collection))

# Add multiple items to a list
my_collection.extend(["More", "Items"])
print(my_collection)

# Add single item to a list
my_collection.append("Single")
print(my_collection)

# Delete the object of a list at a specified index
del(my_collection[2])
print(my_collection)

# Clone a list
clone = my_collection[:]
print(clone)

# Concatenate two lists
my_collection_2 = ["a", "b", "c"]
my_collection_3 = my_collection + my_collection_2
print(my_collection_3)

# Calculate the sum of a list of ints or floats
number_collection = [1, 2, 3, 4, 5]
print(sum(number_collection))

#Check if an item is in a list, returns Boolean
print(1 in my_collection)
print(2 not in my_collection)

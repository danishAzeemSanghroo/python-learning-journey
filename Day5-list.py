global_list = ["apple","banana","grapes","mango"]

# Create a list with 5 numbers and print the list.
items = ["shampo","soap","paste"]
print(items)


# Access and print the first and last elements of a list.
print(global_list[0:1], "and" , global_list[-1:])

# Slice a list to get the first 3 elements.
print(global_list[0:3])

# Slice a list to get the last 2 elements.
print(global_list[-3:])

# Concatenate two lists.
list1 = ["apple","banana","mango"]
list2 = ["potatoes","tomatoes","lady finger"]
print(list1+list2)

# Repeat a list 3 times using *.
print(global_list*3)

# Find the length of a list using len().
print(len(global_list))

# Add a new element at the end of a list using .append().
global_list.append("cherry")
print(global_list)

# Insert an element at the second position using .insert().
global_list.insert(1,"Watermelon")
print(global_list)

# Remove a specific element from a list using .remove().
global_list.remove("Watermelon")
print(global_list)

# Remove the last element using .pop().
global_list.pop()
print(global_list)

# Find the index of a specific element using .index().
print("mango" in global_list)

# Count how many times a value appears using .count().
print(global_list.count("mango"))

# Sort a list in ascending order using .sort().
numbers = [40, 10, 30, 20]
numbers.sort()
print("Sorted list:", numbers)


# Reverse a list using .reverse().
pnumbers = [10, 20, 30, 40]
numbers.reverse()
print("Reversed list:", numbers)
